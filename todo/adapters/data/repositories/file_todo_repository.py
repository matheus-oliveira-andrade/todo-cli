import json
import json
import os
import tempfile
from sqlite3 import Connection, connect

from todo.application.repositories.todo_repository import TodoRepository
from todo.domain.todo import Todo
from todo.domain.todo_status import TodoStatus


class FileTodoRepository(TodoRepository):
    DB_NAME: str = 'todos.db'

    @staticmethod
    def __db_init() -> Connection:
        temp_dir = tempfile.gettempdir()
        db_file = os.path.join(temp_dir, FileTodoRepository.DB_NAME)

        conn = connect(db_file)

        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS todos (
                               id INTEGER PRIMARY KEY,
                               title TEXT,
                               description TEXT,
                               status TEXT,
                               tags TEXT,
                               todo_id TEXT,
                               created_at TIMESTAMP,
                               modified_at TIMESTAMP
                           )''')

        return conn

    def save(self, todo: Todo) -> bool:
        connection = self.__db_init()
        cursor = connection.cursor()

        tags_str = json.dumps(todo.tags)

        query = """
            INSERT INTO todos (title, description, status, tags, todo_id, created_at, modified_at) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        values = (todo.title, todo.description, str(todo.status.name), tags_str, todo.id, str(todo.created_at),
                  str(todo.modified_at))

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        return True

    def get_all(self) -> list[Todo]:
        connection = self.__db_init()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, description, status, tags, todo_id, created_at, modified_at FROM todos")
        rows = cursor.fetchall()

        todos = []
        for row in rows:
            _, title, description, status_str, tags_str, todo_id, created_at, modified_at = row

            tags = json.loads(tags_str)

            todo = Todo(title, description, TodoStatus[status_str], tags, todo_id, created_at, modified_at)

            todos.append(todo)

        connection.close()

        return todos

    def get_by_todo_id(self, todo_id: str) -> Todo:
        connection = self.__db_init()
        cursor = connection.cursor()

        query = """
            SELECT id, 
                   title, 
                   description, 
                   status, 
                   tags, 
                   todo_id, 
                   created_at, 
                   modified_at 
              FROM todos
              WHERE todo_id = ?
        """

        cursor.execute(query, [todo_id])

        row = cursor.fetchone()

        _, title, description, status_str, tags_str, todo_id, created_at, modified_at = row

        tags = json.loads(tags_str)

        todo = Todo(title, description, TodoStatus[status_str], tags, todo_id, created_at, modified_at)

        return todo

    def update(self, todo: Todo) -> bool:
        connection = self.__db_init()
        cursor = connection.cursor()

        tags_str = json.dumps(todo.tags)

        query = f"""
                    UPDATE todos 
                    SET title = ?, 
                        description = ?, 
                        status = ?, 
                        tags = ?, 
                        created_at = ?, 
                        modified_at = ? 
                    WHERE todo_id = ?              
                    """

        values = [
            todo.title,
            todo.description,
            str(todo.status.name),
            tags_str,
            str(todo.created_at),
            str(todo.modified_at),
            todo.id
        ]

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        return True
