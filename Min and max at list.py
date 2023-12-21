numbers = []
while True:
    numbers.append(int(input('Type any integer number: ')))
    stop = input('Wanna continue? ')
    if stop == 'n':
        break
print(f'The minimum value is {min(numbers)} at the position {numbers.index(min(numbers))}')
print(f'The maximum value is {max(numbers)} at the position {numbers.index(max(numbers))}')
