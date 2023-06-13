from abc import ABC, abstractmethod


class TodoRepository(ABC):
    @abstractmethod
    def save(self, todo) -> bool:
        pass

