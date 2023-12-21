import random
numbers = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10), random.randint(0, 10))
print(f'Aleatory numbers: {numbers}')
print(f'Highest: {max(numbers)}')
print(f'Lowest: {min(numbers)}')
