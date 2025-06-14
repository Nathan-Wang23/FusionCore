from ..main.schema import MemoryDrop
from ..main.memory_log import log_memory, load_memory

def test_log_and_load_memory(tmp_path):
    test_file = tmp_path / "test_memory.jsonl"

    mem = MemoryDrop(
        content="Testing memory log system.",
        tags=["test", "memory"],
        emotion={
            "vector": [0.1, 0.5, 0.3],
            "label_mix": {"calm": 0.8}
        }
    )

    # Monkey-patch the path for testing
    from memory_drop.main.memory_log import MEMORY_LOG_PATH
    MEMORY_LOG_PATH = test_file

    log_memory(mem)
    loaded = load_memory()

    assert len(loaded) == 1
    assert loaded[0]["content"] == "Testing memory log system."
    assert "test" in loaded[0]["tags"]
