from src.domain.todo import Todo
from src.domain.todo import TodoStatus


class TestTodo:
    def test_create_new_should_return_new_todo(self):
        # arrange & act
        todo = Todo.create_new('todo', 'todo description', ['tag1', 'tag2'])

        # assert
        assert todo is not None
        assert todo.title == 'todo'
        assert todo.description == 'todo description'
        assert len(todo.tags) == 2

    def test_mark_as_done_should_correctly_update_status(self):
        # arrange
        todo = Todo.create_new('todo', 'todo description', ['tag1', 'tag2'])

        # act
        todo.mark_as_done()

        # assert
        assert todo.status == TodoStatus.DONE

    def test_is_done_should_return_true_if_status_is_done(self):
        # arrange
        todo = Todo.create_new('todo', 'todo description', ['tag1', 'tag2'])

        # act
        result = todo.is_done()

        # assert
        assert result is False
