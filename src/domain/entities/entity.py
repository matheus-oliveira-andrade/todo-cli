from abc import ABC


class Entity(ABC):
    def __init__(self, id, modified_at, created_at):
        self.id = id;
        self.modified_at = modified_at;
        self.created_at = created_at
