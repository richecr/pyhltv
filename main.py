from py_hltv.Matches import get_matches

m = get_matches()
print(len(m))

print(m[0].id)
print(m[0].team1.name)
print(m[0].team1.id)

print(m[0].team2.name)
print(m[0].team2.id)

print(m[0].date_hour)
print(m[0].event)

print("-------------------")

print(m[1].id)
print(m[1].team1.name)
print(m[1].team1.id)

print(m[1].team2.name)
print(m[1].team2.id)

print(m[1].date_hour)
print(m[1].event)

print("-------------------")

print(m[2].id)
print(m[2].team1.name)
print(m[2].team1.id)

print(m[2].team2.name)
print(m[2].team2.id)

print(m[2].date_hour)
print(m[2].event)

print("-------------------")

print(m[3].id)
print(m[3].team1.name)
print(m[3].team1.id)

print(m[3].team2.name)
print(m[3].team2.id)

print(m[3].date_hour)
print(m[3].event)

print("-------------------")

print(m[4].id)
print(m[4].team1.name)
print(m[4].team1.id)

print(m[4].team2.name)
print(m[4].team2.id)

print(m[4].date_hour)
print(m[4].event)

print("-------------------")

print(m[-3].id)
print(m[-3].team1.name)
print(m[-3].team1.id)

print(m[-3].team2.name)
print(m[-3].team2.id)

print(m[-3].date_hour)
print(m[-3].event)

# print(get_matches())
