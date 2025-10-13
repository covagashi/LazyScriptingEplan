# src/ai/documentation_rag.py
from pathlib import Path
from typing import List, Dict
import logging

# Import the base OptimizedRAG class with all improvements
from .optimized_rag import OptimizedRAG

logger = logging.getLogger(__name__)


class OptimizedDocumentationRAG(OptimizedRAG):
    """Optimized version of DocumentationRAG that reads Markdown files with chunking support."""

    def __init__(self):
        super().__init__(embedding_dim=384)
        self.api_path = Path("src/ai/Knowledge/eplan_docs/Eplan API")
        self.cache_path = Path("src/ai/cache/optimized_docs")
        self.cache_path.mkdir(exist_ok=True, parents=True)

        # Chunking settings for long documents
        self.chunk_size = 400  # words per chunk
        self.chunk_overlap = 50  # overlap between chunks

        self._load_or_build()

    def _load_or_build(self):
        """Load from cache or build new index"""
        if not self.load_cache(self.cache_path):
            logger.info("Cache not found or invalid. Building documentation index...")
            self._build_from_files()
            self.save_cache(self.cache_path)
        else:
            logger.info(f"Loaded documentation cache with {len(self.documents)} chunks")

    def _build_from_files(self):
        """Build index from markdown files with intelligent chunking"""
        documents = []
        texts = []

        logger.info(f"Scanning markdown files in {self.api_path}")

        # Use rglob to find all markdown files recursively
        md_files = list(self.api_path.rglob("*.md"))
        logger.info(f"Found {len(md_files)} markdown files")

        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                if not content.strip():
                    logger.debug(f"Skipping empty file: {md_file.name}")
                    continue

                # Get relative path for reference
                rel_path = str(md_file.relative_to(self.api_path))

                # Chunk the content if it's long
                word_count = len(content.split())

                if word_count > self.chunk_size:
                    # Split into chunks
                    chunks = self.chunk_text(content, self.chunk_size, self.chunk_overlap)
                    logger.debug(f"Split {md_file.name} ({word_count} words) into {len(chunks)} chunks")

                    for chunk_idx, chunk in enumerate(chunks):
                        doc = {
                            'id': len(documents),
                            'path': rel_path,
                            'chunk_id': chunk_idx,
                            'total_chunks': len(chunks),
                            'content': chunk,
                            'type': 'documentation',
                            'source_file': md_file.name
                        }

                        documents.append(doc)
                        texts.append(chunk)
                else:
                    # Small file, don't chunk
                    doc = {
                        'id': len(documents),
                        'path': rel_path,
                        'chunk_id': 0,
                        'total_chunks': 1,
                        'content': content,
                        'type': 'documentation',
                        'source_file': md_file.name
                    }

                    documents.append(doc)
                    texts.append(content)

            except Exception as e:
                logger.error(f"Error loading {md_file}: {e}")

        if documents:
            logger.info(f"Building index with {len(documents)} document chunks from {len(md_files)} files")
            self.build_index(documents, texts)
            logger.info(f"Successfully built documentation index with {len(documents)} chunks")
        else:
            logger.warning("No documents found to index!")

    def search_documentation(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Performs a hybrid search for documentation.

        Args:
            query: Search query
            top_k: Number of results to return

        Returns:
            List of document results with scores
        """
        return self.search(query, top_k)

    def find_action_documentation(self, action_name: str) -> List[Dict]:
        """
        Find specific action documentation.

        DEPRECATED: This method now just performs a regular search.
        Kept for compatibility with agents that might still call it.

        Args:
            action_name: Name of the action to find

        Returns:
            List of document results
        """
        return self.search_documentation(action_name, top_k=3)
