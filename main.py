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
    break
