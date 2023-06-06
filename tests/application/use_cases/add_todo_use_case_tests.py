from src.application.dtos.add_todo_dto import AddTodoDto
from src.application.use_cases.add_todo_use_case import AddTodoUseCase
from src.application.use_cases.ports.todo_repository import TodoRepository

from unittest.mock import Mock
from unittest import TestCase


class TestAddTodoUseCase(TestCase):

    def test_handle_should_create_todo_with_success(self):
        # arrange
        todo_repository_mock = Mock()
        todo_repository_mock.save.side_effect = lambda todo: True

        add_todo_dto = AddTodoDto("title", "description", ['tag1', 'tag2'])

        use_case = AddTodoUseCase(todo_repository_mock)

        # act
        result = use_case.handle(add_todo_dto)

        # assert
        assert result is True
        todo_repository_mock.save.assert_called()

    def test_handle_should_not_create_todo(self):
        # arrange
        todo_repository_mock = Mock()
        todo_repository_mock.save.side_effect = lambda todo: False

        add_todo_dto = AddTodoDto("title", "description", ['tag1', 'tag2'])

        use_case = AddTodoUseCase(todo_repository_mock)

        # act
        result = use_case.handle(add_todo_dto)

        # assert
        assert result is False
        todo_repository_mock.save.assert_called()

