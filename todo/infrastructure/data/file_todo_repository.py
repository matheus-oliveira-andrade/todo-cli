import json
import os
import tempfile
from sqlite3 import Connection, connect

from todo.application.repositories.todo_repository import TodoRepository
from todo.domain.todo import Todo


class FileTodoRepository(TodoRepository):

    @staticmethod
    def __db_init() -> Connection:
        temp_dir = tempfile.gettempdir()

        db_file = os.path.join(temp_dir, 'todos.db')
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

        conn.commit()

        return conn

    def save(self, todo: Todo) -> bool:
        connection = self.__db_init()
        cursor = connection.cursor()

        tags_str = json.dumps(todo.tags)

        cursor.execute(
            "INSERT INTO todos (title, description, status, tags, todo_id, created_at, modified_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (todo.title, todo.description, str(todo.status), tags_str, todo.id, todo.created_at, todo.modified_at))

        return True

    def get_all(self) -> list[Todo]:
        connection = self.__db_init()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, description, status, tags, todo_id, created_at, modified_at FROM todos")
        rows = cursor.fetchall()

        todos = []
        for row in rows:
            title, description, status, tags_str, todo_id, created_at, modified_at = row

            tags = json.loads(tags_str)

            todo = Todo(title, description, status, tags, todo_id, created_at, modified_at)

            todos.append(todo)

        connection.close()

        return todos
