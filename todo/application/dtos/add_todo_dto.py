class AddTodoDto:
    def __init__(self, title: str, description: str, tags: list[str]):
        self.title: str = title
        self.description: str = description
        self.tags: list[str] = tags

