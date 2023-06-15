from todo_cli.application.dtos.add_todo_dto import AddTodoDto
from todo_cli.application.use_cases.add_todo_use_case import AddTodoUseCase

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
        self.assertTrue(result)
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
        self.assertFalse(result)
        todo_repository_mock.save.assert_called()

