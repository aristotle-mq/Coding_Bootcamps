class Department:
    id: int
    title: str

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self) -> str:
        return f'title: {self.title}  id: {self.id}'
