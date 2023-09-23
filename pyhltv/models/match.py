from .team import Team

from pydantic import BaseModel


class Match(BaseModel):
    id: int
    team1: Team
    team2: Team
    event: str
    date_hour: str
