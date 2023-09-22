from time import sleep
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

from ..constants import api


def get_page(url: str) -> BeautifulSoup:
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get(api.BASE_URL + url)
    return BeautifulSoup(markup=driver.page_source, features="html.parser")
