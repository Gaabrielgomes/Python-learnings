people = []
data = []
heavy = light = 0
b = str
while b != 'n':
    data.append(str(input('Name: ')))
    data.append(int(input('Weight: ')))
    if len(people) == 0:
        heavy = light = data[1]
    else:
        if data[1] > heavy:
            heavy = data[1]
        if data[1] < light:
            light = data[1]
    people.append(data[:])
    data.clear()
    b = input('Wanna continue? ')
print(f'The quantity of persons signed is {len(people)}')
for p in people:
    if p[1] == heavy:
        print(f'Heaviest person: {p[0]}. {heavy} is its weight')
for p in people:
    if p[1] == light:
        print(f'Lightest person: {p[0]}. {light} is its weight')
