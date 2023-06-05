from src.domain.entities.entity import Entity
from src.domain.enums.todo_status import TodoStatus

from datetime import datetime
import uuid


class Todo(Entity):

    def __init__(self, title, description, status, tags, todo_id, created_at, modified_at):
        super().__init__(todo_id, created_at, modified_at)

        self.title = title
        self.description = description
        self.status = status
        self.tags = tags

    def mark_as_done(self) -> None:
        self.modified_at = datetime.utcnow().time()
        self.status = TodoStatus.DONE

    def is_done(self) -> bool:
        return self.status == TodoStatus.DONE

    @staticmethod
    def create_new(title, description, tags) -> 'Todo':
        now = datetime.utcnow()
        todo_id = str(uuid.uuid4())

        return Todo(title, description, TodoStatus.PENDING, tags, todo_id, now, now)
