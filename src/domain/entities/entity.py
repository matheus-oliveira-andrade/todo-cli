from abc import ABC


class Entity(ABC):
    def __init__(self, todo_id, modified_at, created_at):
        self.todo_id = todo_id
        self.modified_at = modified_at
        self.created_at = created_at
