from typing import Dict

from requests.models import Response
from ..constants import API

import requests
from bs4 import BeautifulSoup


def get_page(url: str) -> BeautifulSoup:
    headers: Dict[str, str] = {
        "referer": "https://www.hltv.org/stats",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    page: Response = requests.get(API.BASE_URL + url, headers=headers)
    return BeautifulSoup(page.text, 'html.parser')
