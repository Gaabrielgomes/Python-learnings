# Colocações
classification = ('Milwaukee Bucks', 'Boston Celtics', 'Philadelphia 76ers', 'Cleveland Cavaliers',
                  'New York Knicks', 'Brooklyn Nets', 'Atlanta Hawks', 'Miami Heat', 'Chicago Bulls', 'Toronto Raptors')
print(f'The teams at the podium are: {classification[0:3]}\n'
      f'The last 4: {classification[-4:]}\n'
      f'Sorted by name: {sorted(classification)}'
      )
while True:
    search = input("Looking for an specific team? ('n' to finish)\n")
    if search == 'n':
        break
    print(f'{search} is actually at the {classification.index(search)}th position')
