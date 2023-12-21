from time import sleep


def counter():
    n1 = int(input('Start: '))
    n2 = int(input('End: '))
    n3 = int(input('Steps: '))
    while n1 != n2:
        n1 += n3
        print(n1)
        sleep(0.5)


def summ(* num):
    s = 0
    for n in num:
        s += n
    print(f'The sum of {num} is {s}')


def perten(listt):
    position = 0
    while position < len(listt):
        listt[position] *= 10
        position += 1
    print(listt)


counter()
summ(5, 6, 2, 4, 1, 7, 5, 8)
numbers = [1, 2, 3, 4, 5]
perten(numbers)