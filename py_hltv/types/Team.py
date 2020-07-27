class Team:
    def __init__(self, name: str, id: int = None) -> None:
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return self.name
