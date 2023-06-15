from abc import ABC, abstractmethod
from todo_cli.domain.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    def save(self, todo: Todo) -> bool:
        pass

