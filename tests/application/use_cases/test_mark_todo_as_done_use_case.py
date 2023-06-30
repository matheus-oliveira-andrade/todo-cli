from todo.domain.todo import Todo
from todo.application.use_cases.mark_todo_as_done_use_case import MarkTodoAsDoneUseCase

from unittest.mock import Mock
from unittest import TestCase

from todo.domain.todo_status import TodoStatus


class TestMarkTodoAsDoneUseCase(TestCase):
    def test_handle_given_todo_pending_should_return_true(self):
        # arrange
        todo_repository_mock = Mock()

        todo = Todo.create_new("title", "description", ['tag1', 'tag2'])

        todo_repository_mock.get_by_todo_id.side_effect = lambda todo_id: todo
        todo_repository_mock.update.side_effect = lambda _: True

        use_case = MarkTodoAsDoneUseCase(todo_repository_mock)

        # act
        result, message = use_case.handle(todo.id)

        # assert
        self.assertTrue(result)
        self.assertIsNone(message)

        todo_repository_mock.get_by_todo_id.assert_called()
        todo_repository_mock.update.assert_called()

        update_todo_args_called = todo_repository_mock.update.call_args[0][0]
        self.assertEqual(TodoStatus.DONE, update_todo_args_called.status)

    def test_handle_given_todo_done_should_return_false(self):
        # arrange
        todo_repository_mock = Mock()

        todo = Todo.create_new("title", "description", ['tag1', 'tag2'])
        todo.mark_as_done()

        todo_repository_mock.get_by_todo_id.side_effect = lambda todo_id: todo
        todo_repository_mock.update.side_effect = lambda _: True

        use_case = MarkTodoAsDoneUseCase(todo_repository_mock)

        # act
        result, message = use_case.handle(todo.id)

        # assert
        self.assertFalse(result)
        self.assertEqual("already marked as done", message)

        todo_repository_mock.get_by_todo_id.assert_called()
        todo_repository_mock.update.assert_not_called()

