class Team:
    def __init__(self, name: str, id: int = None, logo_url: str = "") -> None:
        self.name = name
        self.id = id
        self.logo_url = logo_url

    def __str__(self) -> str:
        return self.name
