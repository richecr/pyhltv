from selenium_stealth import stealth
import undetected_chromedriver as uc


def get_driver():
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    driver = uc.Chrome(options=options)
    stealth(
        driver,
        languages=["en-US", "en"],
        platform="Win32",
        fix_hairline=True,
    )
    return driver
