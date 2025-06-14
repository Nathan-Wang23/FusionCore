from dataclasses import dataclass, field
from typing import List, Dict, Any
from uuid import uuid4
from datetime import datetime

@dataclass
class MemoryDrop:
    id: str = field(default_factory=lambda: f"mem_{datetime.utcnow().isoformat()}_{uuid4().hex[:4]}")
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    input_type: str = "text"  # Could also be vision, audio, etc.
    content: str = ""
    tags: List[str] = field(default_factory=list)
    emotion: Dict[str, Any] = field(default_factory=lambda: {
        "vector": [],
        "label_mix": {}
    })
    recall_score: float = 0.5
    meta: Dict[str, Any] = field(default_factory=dict)
