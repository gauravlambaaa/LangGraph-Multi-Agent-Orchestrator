
from typing import Any, Dict

class Memory:
    """A tiny in-memory store for pipeline data. Replace with Redis or DB for production."""
    def __init__(self):
        self.store: Dict[str, Any] = {}

    def update(self, key: str, value: Any) -> None:
        self.store[key] = value

    def get(self, key: str, default=None):
        return self.store.get(key, default)
