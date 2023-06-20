from abc import ABC
from datetime import datetime


class Entity(ABC):
    def __init__(self, todo_id: str, modified_at: datetime, created_at: datetime):
        self._todo_id = todo_id
        self._modified_at = modified_at
        self._created_at = created_at

    @property
    def id(self) -> str:
        return self._todo_id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def modified_at(self) -> datetime:
        return self._modified_at
