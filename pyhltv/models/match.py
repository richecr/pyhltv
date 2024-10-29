from pydantic import BaseModel

from .team import Team


class Match(BaseModel):
    id: int
    team1: Team
    team2: Team
    event: str
    date_hour: str
