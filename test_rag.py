#!/usr/bin/env python
"""
Test script for Cross-Encoder re-ranking functionality.

This script tests the new re-ranking feature to ensure it improves
search result quality.
"""

import logging
from src.ai.optimized_rag import OptimizedScriptRAG
from src.ai.documentation_rag import OptimizedDocumentationRAG

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

def test_script_search_with_reranking():
    """Test script search with and without re-ranking"""
    print("\n" + "="*70)
    print("TESTING SCRIPT SEARCH WITH RE-RANKING")
    print("="*70 + "\n")

    # Initialize RAG with re-ranking enabled
    print("Initializing Script RAG with re-ranking enabled...")
    rag = OptimizedScriptRAG()

    test_queries = [
        "how to open a project",
        "create new page",
        "export to PDF"
    ]

    for query in test_queries:
        print(f"\n{'-'*70}")
        print(f"Query: '{query}'")
        print(f"{'-'*70}")

        # Search WITHOUT re-ranking
        print("\n[WITHOUT RE-RANKING]")
        results_no_rerank = rag.search(query, top_k=3, use_reranking=False)

        for i, result in enumerate(results_no_rerank, 1):
            example = result['document'].get('example', {})
            score = result.get('score', 0)
            print(f"  {i}. {example.get('name', 'N/A')[:50]} (score: {score:.4f})")

        # Search WITH re-ranking
        print("\n[WITH RE-RANKING]")
        results_rerank = rag.search(query, top_k=3, use_reranking=True)

        for i, result in enumerate(results_rerank, 1):
            example = result['document'].get('example', {})
            score = result.get('score', 0)
            original_score = result.get('original_score', 0)
            print(f"  {i}. {example.get('name', 'N/A')[:50]}")
            print(f"     Cross-Encoder: {score:.4f} | Original: {original_score:.4f}")


def test_documentation_search_with_reranking():
    """Test documentation search with and without re-ranking"""
    print("\n" + "="*70)
    print("TESTING DOCUMENTATION SEARCH WITH RE-RANKING")
    print("="*70 + "\n")

    # Initialize RAG with re-ranking enabled
    print("Initializing Documentation RAG with re-ranking enabled...")
    rag = OptimizedDocumentationRAG()

    test_queries = [
        "Action.Execute method",
        "how to access project settings",
        "device management functions"
    ]

    for query in test_queries:
        print(f"\n{'-'*70}")
        print(f"Query: '{query}'")
        print(f"{'-'*70}")

        # Search WITHOUT re-ranking
        print("\n[WITHOUT RE-RANKING]")
        results_no_rerank = rag.search(query, top_k=3, use_reranking=False)

        for i, result in enumerate(results_no_rerank, 1):
            doc = result['document']
            score = result.get('score', 0)
            path = doc.get('path', 'N/A')
            print(f"  {i}. {path[:60]} (score: {score:.4f})")

        # Search WITH re-ranking
        print("\n[WITH RE-RANKING]")
        results_rerank = rag.search(query, top_k=3, use_reranking=True)

        for i, result in enumerate(results_rerank, 1):
            doc = result['document']
            score = result.get('score', 0)
            original_score = result.get('original_score', 0)
            path = doc.get('path', 'N/A')
            print(f"  {i}. {path[:60]}")
            print(f"     Cross-Encoder: {score:.4f} | Original: {original_score:.4f}")


def check_reranking_status():
    """Check if re-ranking is available"""
    print("\n" + "="*70)
    print("CHECKING RE-RANKING STATUS")
    print("="*70 + "\n")

    rag = OptimizedScriptRAG()

    print(f"Re-ranking enabled: {rag.use_reranker}")
    print(f"Re-ranker model loaded: {rag.reranker_model is not None}")
    print(f"Embedding model loaded: {rag.model is not None}")
    print(f"BM25 index loaded: {rag.bm25_index is not None}")

    stats = rag.get_stats()
    print(f"\nRAG Statistics:")
    print(f"  Documents: {stats['documents']}")
    print(f"  Index type: {stats['index_type']}")
    print(f"  BM25 ready: {stats['bm25_ready']}")

    if rag.use_reranker:
        print(f"\n[+] Re-ranking is ENABLED")
        print(f"  Candidates retrieved: {rag.rerank_candidates}")
        print(f"  Final results: {rag.rerank_final}")
    else:
        print(f"\n[!] Re-ranking is DISABLED")
        print(f"  Hybrid search will be used without Cross-Encoder refinement")


if __name__ == "__main__":
    try:
        # Check status first
        check_reranking_status()

        # Test script search
        test_script_search_with_reranking()

        # Test documentation search
        test_documentation_search_with_reranking()

        print("\n" + "="*70)
        print("[+] ALL TESTS COMPLETED")
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n[X] Error during testing: {e}")
        import traceback
        traceback.print_exc()
