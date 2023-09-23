# from selenium_stealth import stealth
# import undetected_chromedriver as uc

# options = uc.ChromeOptions()
# options.add_argument("--headless=new")
# driver = uc.Chrome(options=options)
# stealth(
#     driver,
#     languages=["en-US", "en"],
#     platform="Win32",
#     fix_hairline=True,
# )
# driver.get("https://www.hltv.org/matches")
# print(driver.page_source)

# Import Matches features from the library
from pyhltv import get_matches

# Return the List of Matches.
matches = get_matches()
print(len(matches))

for i in range(len(matches)):
    match = matches[i]

    print(match.id)
    print(match.team1.name)
    print(match.team1.id)
    print(match.team1.logo_url)

    print(match.team2.name)
    print(match.team2.id)
    print(match.team2.logo_url)

    print(match.date_hour)
    print(match.event)

    print("-------------------")
