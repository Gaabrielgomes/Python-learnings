# Four players and a dice
from random import randint
from time import sleep
from operator import itemgetter
game = dict()
for c in range(1, 5):
    game[f'Player{c}'] = randint(1, 20)
    print(f"Player {c} got {game[f'Player{c}']}")
    sleep(1)
rank = sorted(game.items(), key=itemgetter(1), reverse=True)
for rn, rv in enumerate(rank):
    print(f"{rn+1}° place: {rv[0]} --- {rv[1]}")
    sleep(0.5)
