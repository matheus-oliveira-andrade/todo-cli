import unittest

from todo_cli.domain.todo import Todo
from todo_cli.domain.todo import TodoStatus


class TestTodo(unittest.TestCase):
    def test_create_new_should_return_new_todo(self):
        # arrange & act
        todo = Todo.create_new('todo', 'todo description', ['tag1', 'tag2'])

        # assert
        self.assertIsNotNone(todo)
        self.assertEqual('todo', todo.title)
        self.assertEqual('todo description', todo.description)
        self.assertEqual(2, len(todo.tags))

    def test_mark_as_done_should_correctly_update_status(self):
        # arrange
        todo = Todo.create_new('todo', 'todo description', ['tag1', 'tag2'])

        # act
        todo.mark_as_done()

        # assert
        self.assertEqual(TodoStatus.DONE, todo.status)

    def test_is_done_should_return_true_if_status_is_done(self):
        # arrange
        todo = Todo.create_new('todo', 'todo description', ['tag1', 'tag2'])

        # act
        result = todo.is_done()

        # assert
        self.assertFalse(result)
