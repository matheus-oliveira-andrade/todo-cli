from todo.domain.entity import Entity
from todo.domain.todo_status import TodoStatus

from datetime import datetime
import uuid


class Todo(Entity):

    def __init__(self, title: str, description: str, status: TodoStatus, tags: list[str], todo_id: str, created_at: datetime, modified_at: datetime):
        super().__init__(todo_id, created_at, modified_at)

        self.__title: str = title
        self.__description: str = description
        self.__status: TodoStatus = status
        self.__tags: list[str] = tags

    def mark_as_done(self) -> None:
        self._modified_at = datetime.utcnow()
        self.__status = TodoStatus.DONE

    def is_done(self) -> bool:
        return self.__status == TodoStatus.DONE

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def tags(self):
        return self.__tags

    @property
    def status(self):
        return self.__status

    @staticmethod
    def create_new(title: str, description: str, tags: list[str]) -> 'Todo':
        now = datetime.utcnow()
        todo_id = str(uuid.uuid4())

        return Todo(title, description, TodoStatus.PENDING, tags, todo_id, now, now)
