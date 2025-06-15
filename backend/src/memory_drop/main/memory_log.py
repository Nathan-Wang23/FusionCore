import json
from pathlib import Path
from memory_drop.main.schema import MemoryDrop
from memory_drop.main.constants import MEMORY_LOG_PATH

def log_memory(memory: MemoryDrop, path: Path = MEMORY_LOG_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(memory.__dict__) + "\n")

def load_memory(path: Path = MEMORY_LOG_PATH) -> list:
    if not path.exists():
        return []
    with path.open("r") as f:
        return [json.loads(line) for line in f]
