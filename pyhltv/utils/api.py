from bs4 import BeautifulSoup

from ..constants import api
from ..driver import get_driver


def get_page(url: str) -> BeautifulSoup:
    driver = get_driver()
    driver.get(api.BASE_URL + url)
    return BeautifulSoup(markup=driver.page_source, features="html.parser")
