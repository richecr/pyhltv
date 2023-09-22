from .team import Team


class Match:
    def __init__(
        self, id: int, team1: Team, team2: Team, event, date_hour: str
    ) -> None:
        self.id = id
        self.team1 = team1
        self.team2 = team2
        self.event = event
        self.date_hour = date_hour
