from bs4 import BeautifulSoup

from ..driver import get_driver
from ..constants import api


def get_page(url: str) -> BeautifulSoup:
    driver = get_driver()
    driver.get(api.BASE_URL + url)
    return BeautifulSoup(markup=driver.page_source, features="html.parser")
