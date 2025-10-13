#!/usr/bin/env python
"""
One-time setup script to download the embedding model.

This script downloads the sentence-transformers model once and caches it
locally within the project directory. After running this once, the RAG
system will work completely offline.

Requirements:
- Internet connection (only for this one-time download)
- ~90MB disk space
- 2-5 minutes depending on connection speed

Run this script:
1. From a machine with open internet (not behind corporate VPN)
2. OR from a personal hotspot/home network
3. Only ONCE - the model will be cached permanently

After this, you can:
- Work completely offline
- Share the entire project folder with the model
- Commit to Git (model cache is in .gitignore by default)
"""

import logging
from pathlib import Path
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def download_model():
    """Download and cache the embedding model locally"""

    print("="*70)
    print("EMBEDDING MODEL SETUP")
    print("="*70)
    print("\nThis will download the sentence-transformers model (~90MB)")
    print("You only need to run this ONCE.\n")

    # Define local model path
    local_model_path = Path("src/ai/models/all-MiniLM-L6-v2")
    local_model_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if already exists
    if local_model_path.exists():
        print(f"✓ Model already exists at: {local_model_path}")
        print("\nYou're all set! The RAG system will use this cached model.")
        return True

    try:
        from sentence_transformers import SentenceTransformer

        print("\n📥 Downloading model from HuggingFace...")
        print("   This may take 2-5 minutes depending on your connection.\n")

        # Download model
        model = SentenceTransformer('all-MiniLM-L6-v2')

        print("\n💾 Saving model to local project directory...")
        # Save to local directory
        model.save(str(local_model_path))

        print(f"\n✓ Model successfully cached at: {local_model_path}")
        print(f"   Size: ~90MB")

        # Verify it works
        print("\n🧪 Testing model...")
        test_embedding = model.encode(["test sentence"])
        print(f"✓ Model works! Embedding dimension: {len(test_embedding[0])}")

        print("\n" + "="*70)
        print("✓ SETUP COMPLETE!")
        print("="*70)
        print("\nThe RAG system is now ready to use offline.")
        print("You can now:")
        print("  1. Work without internet connection")
        print("  2. Run rebuild_rag_caches.py to build indexes")
        print("  3. Share this project folder with others")

        return True

    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        print("\n❌ Error: sentence-transformers not installed")
        print("\nPlease install requirements first:")
        print("  pip install -r requirements.txt")
        return False

    except Exception as e:
        logger.error(f"Failed to download model: {e}")
        print("\n❌ Error: Could not download model")
        print("\nPossible causes:")
        print("  1. No internet connection")
        print("  2. Corporate firewall/VPN blocking HuggingFace")
        print("  3. SSL certificate issues")
        print("\nSolutions:")
        print("  1. Try from a different network (home/hotspot)")
        print("  2. Temporarily disable VPN")
        print("  3. Ask a colleague to run this and share the src/ai/models/ folder")
        print("\nNote: The RAG will still work in BM25-only mode without the model,")
        print("      but vector search will be disabled.")
        return False


def check_dependencies():
    """Check if required packages are installed"""
    print("Checking dependencies...")

    required = [
        'sentence_transformers',
        'numpy',
        'faiss',
        'rank_bm25'
    ]

    missing = []
    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} - MISSING")
            missing.append(package)

    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("\nInstall with:")
        print("  pip install -r requirements.txt")
        return False

    print("\n✓ All dependencies installed\n")
    return True


def main():
    """Main execution"""
    print()

    # Check dependencies first
    if not check_dependencies():
        return 1

    # Download model
    if not download_model():
        return 1

    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)
