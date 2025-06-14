import json
from pathlib import Path
from memory_drop.main.schema import MemoryDrop

MEMORY_LOG_PATH = Path("backend/data/memory_log.jsonl")

def log_memory(memory: MemoryDrop):
    MEMORY_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MEMORY_LOG_PATH.open("a") as f:
        f.write(json.dumps(memory.__dict__) + "\n")

def load_memory() -> list:
    if not MEMORY_LOG_PATH.exists():
        return []
    with MEMORY_LOG_PATH.open("r") as f:
        return [json.loads(line) for line in f]
