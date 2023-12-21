def file(n='No player', g=0):
    print(f'Player: {n}\nGoals:{g}')


name = str(input('Player name: '))
goals = input('Goals: ')
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    file(g=goals)
else:
    file(name, goals)
