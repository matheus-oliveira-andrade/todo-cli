from todo_cli.domain.entity import Entity
from todo_cli.domain.todo_status import TodoStatus

from datetime import datetime
import uuid


class Todo(Entity):

    def __init__(self, title, description, status, tags, todo_id, created_at, modified_at):
        super().__init__(todo_id, created_at, modified_at)

        self.__title = title
        self.__description = description
        self.__status = status
        self.__tags = tags

    def mark_as_done(self) -> None:
        self._modified_at = datetime.utcnow().time()
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
    def create_new(title, description, tags) -> 'Todo':
        now = datetime.utcnow()
        todo_id = str(uuid.uuid4())

        return Todo(title, description, TodoStatus.PENDING, tags, todo_id, now, now)
