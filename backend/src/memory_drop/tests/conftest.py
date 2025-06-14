import pytest
from pathlib import Path
from ..main.schema import MemoryDrop

BASE_TEST_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_TEST_DIR / "data"

@pytest.fixture
def test_memory():
    return MemoryDrop(
        content="Testing memory log system.",
        tags=["test", "memory"],
        emotion={
            "vector": [0.1, 0.5, 0.3],
            "label_mix": {"calm": 0.8}
        }
    )

@pytest.fixture
def data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR

@pytest.fixture
def get_test_log_path(data_dir):
    def _get_path(name: str) -> Path:
        path = data_dir / f"{name}.jsonl"
        path.write_text("")
        return path
    return _get_path
