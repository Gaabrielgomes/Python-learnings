grades = [[], [], []]
c = 0
print(f"{'Grades system':.^30}")
while True:
    name = input("Student's name: ")
    n1 = float(input('Grade 1: '))
    n2 = float(input('Grade 2: '))
    grades[0].append(name)
    grades[1].append(n1)
    grades[2].append(n2)
    breaker = input('Wanna add another student?(Space/n)')
    if breaker == 'n':
        break
print(f"{'School bulletin':.^30}")
print(f"{'Name':.<10}", end=' ')
print(f"{'Grade 1':.>5}", end=' ')
print(f"{'Grade 2':.>5}")
for c in range(0, len(grades)):
    print(f'{grades[0][c]:.<10}', end=' ')
    print(f'{grades[1][c]:>5}', end=' ')
    print(f'{grades[2][c]:>6}')
    c += 1
