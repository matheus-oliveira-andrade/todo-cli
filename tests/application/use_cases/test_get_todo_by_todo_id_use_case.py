from todo.domain.todo import Todo
from todo.application.use_cases.get_todo_by_todo_id_use_case import GetTodoByTodoIdUseCase

from unittest.mock import Mock
from unittest import TestCase


class TestGetTodoByTodoIdUseCase(TestCase):
    def test_handle_should_return_todo(self):
        # arrange
        todo_repository_mock = Mock()

        todo = Todo.create_new("title", "description", ['tag1', 'tag2'])

        todo_repository_mock.get_by_todo_id.side_effect = lambda todo_id: todo

        use_case = GetTodoByTodoIdUseCase(todo_repository_mock)

        # act
        result = use_case.handle(todo.id)

        # assert
        self.assertIsNotNone(result)
        self.assertEqual(result, todo)

        todo_repository_mock.get_by_todo_id.assert_called()

    def test_handle_when_not_found_todos_should_return_empty(self):
        # arrange
        todo_repository_mock = Mock()
        todo_repository_mock.get_by_todo_id.side_effect = lambda todo_id: None

        use_case = GetTodoByTodoIdUseCase(todo_repository_mock)

        # act
        result = use_case.handle("123321")

        # assert
        self.assertIsNone(result)

        todo_repository_mock.get_by_todo_id.assert_called()
