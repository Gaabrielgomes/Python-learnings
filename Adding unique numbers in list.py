val = []
c = 0
while True:
    n = int(input('Add an integer number '))
    if n not in val:
        if c == 0 or n > val[-1]:
            val.append(n)
            c += 1
        else:
            p = 0
            while p < len(val):
                if n <= val[p]:
                    val.insert(p, n)
                    break
                p += 1
    else:
        print('A number cannot be added twice')
    b = input('Wanna continue? (Enter/n) ')
    if b == 'n':
        break
print(f'The final list is {val}')
