from memory_drop.main.schema import MemoryDrop
from memory_drop.main.embed import generate_embedding
from memory_drop.main.memory_log import log_memory
from memory_drop.main.constants import MEMORY_LOG_PATH
from pathlib import Path
from typing import List

def handle_user_input(content: str, input_type: str = "text", tags: List[str] = None, log_path: Path = MEMORY_LOG_PATH) -> MemoryDrop:
    if tags is None:
        tags = []

    embedding = generate_embedding(content)

    memory = MemoryDrop(
        content=content,
        input_type=input_type,
        tags=tags,
        meta={"input_length": len(content)},
    )
    memory.meta["embedding"] = embedding.tolist()  # Store for now

    log_memory(memory, path=log_path)
    return memory
