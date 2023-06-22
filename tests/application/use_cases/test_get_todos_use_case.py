from todo.domain.todo import Todo
from todo.application.use_cases.get_todos_use_case import GetTodosUseCase

from unittest.mock import Mock
from unittest import TestCase


class TestGetTodosUseCase(TestCase):
    def test_handle_should_return_todos(self):
        # arrange
        todo_repository_mock = Mock()

        todo_one = Todo.create_new("title", "description", ['tag1', 'tag2'])
        todo_two = Todo.create_new("title2", "description2", ['tag1'])

        todos = [todo_one, todo_two]

        todo_repository_mock.get_all.side_effect = lambda: todos

        use_case = GetTodosUseCase(todo_repository_mock)

        # act
        result = use_case.handle()

        # assert
        self.assertListEqual(result, todos)

        todo_repository_mock.get_all.assert_called()

    def test_handle_when_not_found_todos_should_return_empty(self):
        # arrange
        todo_repository_mock = Mock()
        todo_repository_mock.get_all.side_effect = lambda: None

        use_case = GetTodosUseCase(todo_repository_mock)

        # act
        result = use_case.handle()

        # assert
        self.assertIsNotNone(result)
        self.assertListEqual(result, [])

        todo_repository_mock.get_all.assert_called()
