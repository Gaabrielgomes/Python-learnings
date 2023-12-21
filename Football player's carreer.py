from time import sleep


def line():
    print('~' * 30)


players = dict()
team = list()
matches = list()
while True:
    players.clear()
    players['name'] = input("Player's name: ")
    matchesp = int(input(f"How many matches did {players['name']} played? "))
    for c in range(0, matchesp):
        matches.append(int(input(f"How many goals at the match number {c+1}? ")))
    players['goals'] = matches[:]
    players['mplayed'] = matchesp
    players['tgoals'] = sum(players['goals'])
    team.append(players.copy())
    matches.clear()
    breaker = str(input('Any more players? [space(y)/(n)]'))
    if breaker == 'n':
        break
line()
print(f"{'Table of results':.^28}")
line()
print('Code', end='')
for i in players.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(team):
    print(f"\n{k:>3}", end='')
    for i in v.values():
        print(f"{str(i):<15}", end='')
    print()
while True:
    line()
    search = int(input("Search for a player if you want('999' to end): "))
    if search == 999:
        print('<End of the code>')
        break
    elif search > len(team):
        print('There is no player with this number')
    else:
        print(f"Player n°{search}, {team[search]['name']}")
        for k, v in enumerate(team[search]['goals']):
            print(f'At the match {k}, made {v} goal(s)')
            sleep(0.5)
# Not self-made :(
