from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any
from pathlib import Path

from memory_drop.main.schema import MemoryDrop
from memory_drop.main.input_handler import handle_user_input
from memory_drop.main.memory_log import load_memory
from memory_drop.main.constants import MEMORY_LOG_PATH

router = APIRouter()

# Request body model
class MemoryDropIn(BaseModel):
    content: str
    input_type: str = "text"
    tags: List[str] = []

class MemoryDropOut(MemoryDropIn):
    id: str
    timestamp: str
    emotion: Dict[str, Any]
    recall_score: float
    meta: Dict[str, Any]

# POST /memory — create and log a memory
@router.post("/", response_model=MemoryDropOut)
def create_memory(input: MemoryDropIn):
    memory = handle_user_input(
        content=input.content,
        input_type=input.input_type,
        tags=input.tags,
        log_path=MEMORY_LOG_PATH
    )
    return memory

# GET /memory — retrieve all logged memories
@router.get("/", response_model=List[dict])
def get_memories():
    return load_memory(path=MEMORY_LOG_PATH)
