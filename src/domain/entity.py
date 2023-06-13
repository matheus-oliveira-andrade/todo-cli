from abc import ABC


class Entity(ABC):
    def __init__(self, todo_id, modified_at, created_at):
        self._todo_id = todo_id
        self._modified_at = modified_at
        self._created_at = created_at
