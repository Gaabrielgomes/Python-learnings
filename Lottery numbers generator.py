import time
import random
games = []
bets = []
print(f"{'Lottery':~^30}")
quant = int(input('How many games do you need? '))
c = 0
while c < quant:
    n = 0
    while n < 6:
        num = random.randint(1, 60)
        if n == 0 or num not in bets:
            bets.append(num)
            n += 1
    games.append(bets[:])
    print(f'Game {c+1}: {games[c]}')
    bets.clear()
    c += 1
    time.sleep(1.2)
print(f"{'Bets ready, good luck!':~^30}")
