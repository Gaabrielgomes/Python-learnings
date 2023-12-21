def factorial(num):
    from time import sleep
    c = 1
    for n in range(num, 0, -1):
        if n > 1:
            print(n, 'x ', end='')
            sleep(0.8)
        else:
            sleep(0.8)
            print(n, '= ', end='')
        c *= n
    return c


print(factorial(int(input('Integer number to do factorial: '))))
