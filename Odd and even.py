values = []
numbers = []
b = str
while b != 'n':
    numbers.append(int(input('Type any number: ')))
    values.append(numbers[:])
    numbers.clear()
    b = input('Wanna continue? ')
print('The even numbers are: ')
for even in range(len(values)):
    if even % 2 == 0:
        print(f'{even}')
print('The odd numbers are: ')
for odd in range(len(values)):
    if odd % 2 != 0:
        print(f'{odd}')
