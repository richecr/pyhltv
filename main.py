from py_hltv.Matches import get_matches

matches = get_matches()
print(len(matches))

for i in range(0, len(matches)):
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
