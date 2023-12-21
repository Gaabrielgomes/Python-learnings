enh = ('Fighter', 10000, 'Wizard', 10000, 'Lucky', 10000,
       'Healer', 10000, 'Hybrid', 10000, 'Thief', 10000,
       'Spellbreaker', 10000)
print(f'{"Enchancements":=^35}')
for position in range(0, len(enh)):
    if position % 2 == 0:
        print(f'{enh[position]:.<25}', end='')
    else:
        print(f'${enh[position]:>5.2f}')
print(f'{"Not self-made":=^35}')
