from sentence_transformers import SentenceTransformer
import numpy as np

# Load once on import
_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str) -> np.ndarray:
    return _model.encode(text, normalize_embeddings=True)
