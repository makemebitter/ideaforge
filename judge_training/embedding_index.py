"""
Phase 3: Embedding Index for Paper Retrieval

Embeds all papers (title + abstract) using a local sentence-transformer model
and builds a FAISS index for fast nearest-neighbor search.

At evaluation time: embed the current idea -> retrieve top-K most similar
published papers -> inject their metadata + review highlights into context.

Usage:
    python embedding_index.py                   # Build index from all data
    python embedding_index.py --model all-MiniLM-L6-v2  # Use a different model
    python embedding_index.py --top-k 5 --query "video diffusion with attention"  # Test query
"""

import json
import argparse
import functools
import os
from pathlib import Path

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

print = functools.partial(print, flush=True)  # type: ignore

BASE_DIR = Path(__file__).parent
_RESOURCES_DIR = os.environ.get("IDEAFORGE_RESOURCES_DIR")
if _RESOURCES_DIR:
    DATA_DIR = Path(_RESOURCES_DIR) / "data"
    EMBED_DIR = Path(_RESOURCES_DIR) / "embeddings"
else:
    DATA_DIR = BASE_DIR / "data"
    EMBED_DIR = BASE_DIR / "embeddings"

DEFAULT_MODEL = "all-MiniLM-L6-v2"


def load_all_papers() -> list[dict]:
    """Load both train and test splits."""
    papers = []
    for split in ["train.jsonl", "test.jsonl"]:
        path = DATA_DIR / split
        if not path.exists():
            continue
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                papers.append(json.loads(line))
    return papers


def prepare_texts(papers: list[dict]) -> list[str]:
    """Prepare text for embedding: title + abstract."""
    texts = []
    for p in papers:
        title = p.get("title", "")
        abstract = p.get("abstract", "")
        kw = " ".join(p.get("keywords", []))
        text = f"{title}. {abstract}"
        if kw:
            text += f" Keywords: {kw}"
        texts.append(text[:2000])
    return texts


def prepare_metadata(papers: list[dict]) -> list[dict]:
    """Prepare lightweight metadata to store alongside embeddings."""
    meta = []
    for p in papers:
        review_summary = ""
        if p.get("review_texts"):
            strengths = []
            weaknesses = []
            for rev in p["review_texts"][:3]:
                s = rev.get("strengths", "")
                w = rev.get("weaknesses", "")
                if s:
                    strengths.append(s[:200])
                if w:
                    weaknesses.append(w[:200])
            if strengths:
                review_summary += "Strengths: " + " | ".join(strengths)[:400]
            if weaknesses:
                review_summary += " Weaknesses: " + " | ".join(weaknesses)[:400]

        meta.append({
            "paper_id": p.get("paper_id", ""),
            "title": p.get("title", ""),
            "abstract_snippet": p.get("abstract", "")[:300],
            "venue": p.get("venue", ""),
            "year": p.get("year"),
            "avg_rating": p.get("avg_rating", 0),
            "decision": p.get("decision", ""),
            "num_reviews": p.get("num_reviews", 0),
            "review_summary": review_summary[:800],
            "pdf_path": p.get("pdf_path"),
            "forum_url": p.get("forum_url", ""),
        })
    return meta


def build_index(model_name: str = DEFAULT_MODEL, batch_size: int = 256):
    """Build the FAISS index and save metadata."""
    EMBED_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading papers...")
    papers = load_all_papers()
    print(f"  {len(papers)} papers loaded")

    texts = prepare_texts(papers)
    metadata = prepare_metadata(papers)

    print(f"Loading model: {model_name}...")
    model = SentenceTransformer(model_name)
    dim = model.get_sentence_embedding_dimension()
    print(f"  Embedding dimension: {dim}")

    print(f"Encoding {len(texts)} papers (batch_size={batch_size})...")
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    print(f"  Embeddings shape: {embeddings.shape}")

    print("Building FAISS index (IndexFlatIP for cosine similarity)...")
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype(np.float32))
    print(f"  Index size: {index.ntotal} vectors")

    faiss_path = EMBED_DIR / "paper_embeddings.faiss"
    faiss.write_index(index, str(faiss_path))
    print(f"  Saved FAISS index to {faiss_path}")

    meta_path = EMBED_DIR / "embedding_metadata.jsonl"
    with open(meta_path, "w", encoding="utf-8") as f:
        for m in metadata:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"  Saved metadata to {meta_path}")

    config = {
        "model_name": model_name,
        "embedding_dim": dim,
        "num_papers": len(papers),
        "index_type": "IndexFlatIP",
    }
    config_path = EMBED_DIR / "config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    print(f"  Saved config to {config_path}")

    return index, metadata, model


def query_index(query: str, top_k: int = 5,
                model_name: str = DEFAULT_MODEL) -> list[dict]:
    """Query the index and return top-K most similar papers."""
    faiss_path = EMBED_DIR / "paper_embeddings.faiss"
    meta_path = EMBED_DIR / "embedding_metadata.jsonl"
    config_path = EMBED_DIR / "config.json"

    if not faiss_path.exists():
        raise FileNotFoundError(f"Run build_index first: {faiss_path}")

    with open(config_path, "r") as f:
        config = json.load(f)

    model = SentenceTransformer(config["model_name"])
    index = faiss.read_index(str(faiss_path))

    metadata = []
    with open(meta_path, "r", encoding="utf-8") as f:
        for line in f:
            metadata.append(json.loads(line))

    q_emb = model.encode([query], normalize_embeddings=True).astype(np.float32)
    scores, indices = index.search(q_emb, top_k)

    results = []
    for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
        if idx < 0 or idx >= len(metadata):
            continue
        meta = metadata[idx].copy()
        meta["similarity_score"] = float(score)
        meta["rank"] = i + 1
        results.append(meta)

    return results


def format_retrieval_context(results: list[dict]) -> str:
    """Format retrieved papers into context string for the judge."""
    lines = ["## Similar Published Papers (retrieved by embedding similarity)\n"]
    for r in results:
        lines.append(f"### [{r['rank']}] {r['title']}")
        lines.append(f"**Score: {r['avg_rating']:.1f}/10** | "
                      f"Decision: {r.get('decision', '?')} | "
                      f"Venue: {r.get('venue', '?')} {r.get('year', '')}")
        if r.get("abstract_snippet"):
            lines.append(f"Abstract: {r['abstract_snippet']}...")
        if r.get("review_summary"):
            lines.append(f"Reviews: {r['review_summary']}")
        lines.append(f"Similarity: {r['similarity_score']:.3f}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Build/query paper embedding index")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL,
                        help=f"Sentence-transformer model (default: {DEFAULT_MODEL})")
    parser.add_argument("--batch-size", type=int, default=256,
                        help="Batch size for encoding (default: 256)")
    parser.add_argument("--query", type=str, default=None,
                        help="Test query to run against the index")
    parser.add_argument("--top-k", type=int, default=5,
                        help="Number of results to return for query")
    parser.add_argument("--build-only", action="store_true",
                        help="Only build the index, don't run a test query")
    args = parser.parse_args()

    if args.query:
        results = query_index(args.query, top_k=args.top_k, model_name=args.model)
        print(format_retrieval_context(results))
        return

    index, metadata, model = build_index(model_name=args.model, batch_size=args.batch_size)

    if not args.build_only:
        print("\n" + "=" * 60)
        print("TEST QUERY: 'video generation with diffusion models'")
        print("=" * 60)
        q = "video generation with diffusion models and temporal consistency"
        q_emb = model.encode([q], normalize_embeddings=True).astype(np.float32)
        scores, indices = index.search(q_emb, 5)
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx >= 0 and idx < len(metadata):
                m = metadata[idx]
                print(f"  [{i+1}] score={score:.3f} | rating={m['avg_rating']} | {m['title'][:70]}")


if __name__ == "__main__":
    main()
