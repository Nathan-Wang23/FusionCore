from memory_drop.main.embed import generate_embedding
import numpy as np

def test_generate_embedding():
    test_text = "This is a test sentence."
    embedding = generate_embedding(test_text)

    assert embedding is not None
    assert isinstance(embedding, np.ndarray)
    assert embedding.shape[0] > 0
