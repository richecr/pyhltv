import time
from typing import List, Tuple,  Union

from bs4.element import Tag

from .models.Team import Team
from .models.Match import Match
from .utils.api import get_page


def get_matches() -> List[Match]:
    """
    Function that searches for the information of all matches.

    RETURN:
    ----------
    matches: List[Match]
    """
    soup = get_page('/matches')
    rounds_upcommingMatch: List[Tag] = soup.findAll(
        'div', {'class': 'upcomingMatch'})
    rounds_live: List[Tag] = soup.findAll(
        'div', {'class': 'liveMatch-container'})
    rounds = rounds_live + rounds_upcommingMatch

    matches: List[Match] = []
    for div in rounds:
        match = div.findAll('a', {'class': 'match a-reset'})[0]
        id_ = int(match['href'].split('/')[2])
        date_hour: Tag = match.findAll('div', {'class': 'matchTime'})[0]
        event: List[Tag] = match.findAll(
            'div', {'class': 'matchEventName gtSmartphone-only'})
        div_empty = match.findAll('div', {'class': 'matchInfoEmpty'})
        if (div_empty == []):
            team1, team2 = get_teams(div)

            name_event = str(event[0].text) if event != [] else ''
            date_unix = date_hour.text
            if (date_hour.text != 'LIVE'):
                date_unix = date_unix_to_timestamp(date_hour['data-unix'])

            match = Match(id_, team1, team2, name_event, date_unix)
            matches.append(match)

    return matches


def get_teams(match: Tag) -> Tuple[Team, Team]:
    return get_team(match, 0), get_team(match, 1)


def get_team(match: Tag, num_team: int) -> Team:
    """
    Function that seeks and treats the information of a team.

    PARAMS:
    ----------
    `match`: Match in which the team will be found.
    `info_teams_id`: BeautifulSoup list with team ID information.
    `num_team`: The team to be found (0 or 1).

    RETURN:
    ----------
    team: Team
    """
    team: Team
    divs_teams = match.findAll(
        'div', {'class': 'matchTeam'})
    div_team_empty = divs_teams[num_team].findAll(
        'div', {'class': 'team text-ellipsis'})
    if (div_team_empty != []):
        team = Team(div_team_empty[0].text)
    else:
        name = divs_teams[num_team].findAll(
            'div', {'class': 'matchTeamName text-ellipsis'})[0]
        div_id = divs_teams[num_team].findAll(
            'div', {'class': 'matchTeamScore'})
        img_logo_url = divs_teams[num_team].findAll(
            'img', {'class': 'matchTeamLogo'})

        id_team: Union[int, None] = None
        if (div_id == []):
            id_team = match['team{}'.format(num_team + 1)]
        else:
            span_id = div_id[0].findAll(
                'span', {'class': 'currentMapScore'})[0]
            id_team = int(span_id['data-livescore-team'])

        team = Team(name.text, id_team,
                    logo_url=get_logo_url(img_logo_url))

    return team


def get_logo_url(img_logo_url: List) -> str:
    """
    function that obtains the URL of a team's logo.

    PARAMS:
    ----------
    `img_logo_url`: URL logo that verifed and concated.

    RETURN:
    ----------
    `url_logo`: URL concated.
    """
    url_logo = ''
    if (img_logo_url != []):
        url_logo = img_logo_url[0]['src']
        if (url_logo.startswith('/img')):
            url_logo = 'https://www.hltv.org' + url_logo

    return url_logo


def date_unix_to_timestamp(date_unix: str) -> str:
    """
    Function that convert unix date to human-readable date.

    PARAMS:
    ----------
    :param: date_unix: Date in format unix.

    RETURN:
    ----------
    date: str in format(dd b yyyy H:M:S +0000)
        - 08 Aug 2020 16:00:00 +0000
    """
    ts = int(date_unix)
    ts /= 1000
    date_hour = time.strftime(
        "%d %b %Y %H:%M:%S +0000", time.localtime(ts))
    return date_hour
