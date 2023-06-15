from abc import ABC
from datetime import datetime


class Entity(ABC):
    def __init__(self, todo_id: str, modified_at: datetime, created_at: datetime):
        self._todo_id = todo_id
        self._modified_at = modified_at
        self._created_at = created_at
