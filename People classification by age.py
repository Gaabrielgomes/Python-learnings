people = dict()
persons = list()
summ = average = 0
while True:
    people.clear()
    people['name'] = str(input('Name: '))
    while True:
        people['gender'] = str(input('Gender(m/f): ').upper()[0])
        if people['gender'] not in 'FfMm':
            print('Only true genders are accepted')
        else:
            break
    people['age'] = int(input('Age: '))
    persons.append(people.copy())
    summ += people['age']
    breaker = input('Continue?(enter/n) ')
    if breaker == 'n':
        break
average = summ / len(persons)
for c in range(0, len(persons)):
    print(f"{persons[c]}")
print(f"{len(persons)} people were registered")
print(f"The average age is {average:5.2f}")
print('Women: ', end='')
for p in persons:
    if p['gender'] in 'Ff':
        print(f"{p['name']}", end='| ')
print()
print(f"Persons above average age: ", end=' ')
for p in persons:
    if p['age'] > average:
        print(f"{p['name']} |-", end='')
print('\nEnd of the code')
