from time import sleep
num1 = int(input('Type the initial number for an Fibonacci sequence: '))
num2 = int(input('Type the second number of this sequence: '))
ran = int(input('How many times you want to rerun the sum? '))
for c in range(0, ran):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    sleep(1)
    print(num3)
