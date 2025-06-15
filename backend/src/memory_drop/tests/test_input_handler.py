from memory_drop.main.input_handler import handle_user_input
from memory_drop.main.memory_log import load_memory
from memory_drop.main.schema import MemoryDrop

def test_handle_user_input(get_test_log_path):
    test_log_file = get_test_log_path("test_handle_user_input")  # 🎯 Unique path per test

    memory = handle_user_input(
        content="Testing user input handling.",
        input_type="text",
        tags=["unit", "test"],
        log_path=test_log_file
    )

    # Assert the object returned looks correct
    assert isinstance(memory, MemoryDrop)
    assert memory.content == "Testing user input handling."
    assert "unit" in memory.tags

    # Assert it was logged correctly
    loaded = load_memory(path=test_log_file)
    assert len(loaded) == 1
    assert loaded[0]["content"] == "Testing user input handling."
    assert "unit" in loaded[0]["tags"]
