from pydantic import BaseModel


class Team(BaseModel):
    id: int = 0
    name: str = ""
    logo_url: str = ""
