from abc import ABC, abstractmethod
from todo.domain.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    def save(self, todo: Todo) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[Todo]:
        pass

