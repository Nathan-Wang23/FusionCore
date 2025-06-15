from memory_drop.main.schema import MemoryDrop
from memory_drop.main.memory_log import log_memory, load_memory
from pathlib import Path

def test_log_and_load_memory(test_memory, get_test_log_path):
    test_path = get_test_log_path("test_log_and_load_memory")
    log_memory(test_memory, path=test_path)
    loaded = load_memory(path=test_path)

    assert len(loaded) == 1
    assert loaded[0]["content"] == test_memory.content
    assert "test" in loaded[0]["tags"]
