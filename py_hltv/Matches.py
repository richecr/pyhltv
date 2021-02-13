import time
from typing import List, Tuple

from bs4.element import Tag

from .models.Team import Team
from .models.Matches import Matches
from .utils.api import get_page


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


def concat_url_logo_empty(url: str) -> str:
    if (url.startswith('/img')):
        return 'https://www.hltv.org' + url
    return url


def get_logo_url(img_logo_url: List) -> str:
    if (img_logo_url != []):
        return concat_url_logo_empty(img_logo_url[0]['src'])
    else:
        return ''


def get_team(match: Tag, num_team: int) -> Team:
    """
    Function that seeks and treats the information of a team.

    PARAMS:
    ----------
    :param: match: Match in which the team will be found.
    :param: info_teams_id: BeautifulSoup list with team ID information.
    :param: num_team: The team to be found (0 or 1).

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
        if (div_id == []):
            team = Team(name=name.text, logo_url=get_logo_url(img_logo_url))
        else:
            span_id = div_id[0].findAll(
                'span', {'class': 'currentMapScore'})[0]
            id = span_id['data-livescore-team']
            team = Team(name.text, id, logo_url=get_logo_url(img_logo_url))

    return team


def get_teams(match: Tag) -> Tuple[Team, Team]:
    return get_team(match, 0), get_team(match, 1)


def get_matches() -> List[Matches]:
    """
    Function that searches for the information of all matches.

    RETURN:
    ----------
    matches: List[Matches]
    """
    soup = get_page('/matches')
    rodadas: List[Tag] = soup.findAll('a', {'class': 'match a-reset'})

    matches: List[Matches] = []
    for game in rodadas:
        id_ = int(game['href'].split('/')[2])
        date_hour: Tag = game.findAll('div', {'class': 'matchTime'})[0]
        event: List[Tag] = game.findAll(
            'div', {'class': 'matchEventName gtSmartphone-only'})
        div_empty = game.findAll('div', {'class': 'matchInfoEmpty'})
        if (div_empty == []):
            team1, team2 = get_teams(game)

            name_event = str(event[0].text) if event != [] else ''
            date_unix = date_hour.text
            if (date_hour.text != 'LIVE'):
                date_unix = date_unix_to_timestamp(date_hour['data-unix'])

            match = Matches(id_, team1, team2, name_event, date_unix)
            matches.append(match)

    return matches
