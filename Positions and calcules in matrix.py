positions = []
pos = []
add = column = 0
print(f'{"Matrix":.^30}')
for p in range(1, 10):
    if p == 1:
        pos.append(int(input(f'Type the {p}st number: ')))
    if p == 2:
        pos.append(int(input(f'Type the {p}nd number: ')))
    if p == 3:
        pos.append(int(input(f'Type the {p}rd number: ')))
    if p > 3:
        pos.append(int(input(f'Type the {p}th number: ')))
    if p == 2 or p == 5 or p == 8:
        column += p
    positions.append(pos[:])
    pos.clear()
for even in range(len(positions)):
    if even % 2 == 0:
        add += even
if positions[4] < positions[3] > positions[5]:
    biggest = positions[3]
elif positions[3] < positions[4] > positions[5]:
    biggest = positions[4]
else:
    biggest = positions[5]
print(f'{"Number-added matrix":.^30}')
print(f'{positions[0]} {positions[1]} {positions[2]}\n'
      f'{positions[3]} {positions[4]} {positions[5]}\n'
      f'{positions[6]} {positions[7]} {positions[8]}')
print(f'The sum of the even numbers is {add}')
print(f'The sum of the numbers in 3rd column is {column}')
print(f'The biggest number at the 2nd line is {biggest}')
