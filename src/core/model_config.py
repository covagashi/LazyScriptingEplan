# src/core/model_config.py
import os
import logging
from pathlib import Path
from typing import Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class ModelPaths:
    """Configuration for model paths and cache directories"""
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    cache_dir: Optional[str] = None
    local_models_dir: str = "./models"
    
class ModelManager:
    """Professional model path management without hardcoded paths"""
    
    def __init__(self):
        self.config = ModelPaths()
        
    def get_model_cache_path(self) -> Optional[Path]:
        """Automatically detect or configure model cache location"""
        
        # 1. Environment variable (highest priority)
        env_cache = os.getenv('HUGGINGFACE_HUB_CACHE')
        if env_cache:
            cache_path = Path(env_cache) / "sentence-transformers--all-MiniLM-L6-v2"
            if cache_path.exists():
                logger.info(f"Using HF cache from environment: {cache_path}")
                return cache_path
        
        # 2. Standard HuggingFace cache locations
        cache_locations = [
            Path.home() / ".cache" / "huggingface" / "hub" / "models--sentence-transformers--all-MiniLM-L6-v2",
            Path.home() / ".cache" / "huggingface" / "transformers" / "sentence-transformers--all-MiniLM-L6-v2",
            Path.home() / ".cache" / "torch" / "sentence_transformers"
        ]
        
        for location in cache_locations:
            if location.exists():
                logger.info(f"Found cached model at: {location}")
                return location
                
        # 3. Project local models directory
        local_path = Path(self.config.local_models_dir) / "all-MiniLM-L6-v2"
        if local_path.exists():
            logger.info(f"Using local model: {local_path}")
            return local_path
            
        logger.warning("No cached model found, will download on first use")
        return None
    
    def load_sentence_transformer(self):
        """Load SentenceTransformer with robust fallback strategy"""
        from sentence_transformers import SentenceTransformer
        
        try:
            # Try cached model first
            cached_path = self.get_model_cache_path()
            if cached_path and cached_path.exists():
                try:
                    model = SentenceTransformer(str(cached_path))
                    logger.info(f"Loaded cached model from: {cached_path}")
                    return model
                except Exception as cache_error:
                    logger.warning(f"Cache corrupted, removing: {cache_error}")
                    import shutil
                    shutil.rmtree(cached_path, ignore_errors=True)
            
            # Clean download with proper config
            logger.info("Downloading model...")
            model = SentenceTransformer(
                self.config.model_name,
                trust_remote_code=True
            )
            logger.info("Model downloaded successfully")
            return model
            
        except Exception as e:
            logger.error(f"Model loading failed: {e}")
            raise RuntimeError(f"Could not initialize SentenceTransformer: {e}")

# Global instance for reuse
model_manager = ModelManager()