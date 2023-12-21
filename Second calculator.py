# Calculator
import math
import emoji


action = float
while action != 0:
    action = input("Tell the action you want. '0' to exit\n")
    if action == '0':
        print(emoji.emojize('You choose to exit\nBye!:waving_hand:'))
        break
    if action == '!':
        num3 = int(input('Type any integer number '))
        print(math.factorial(num3))
    num = float(input('Type any number '))
    if action == 'log':
        print(math.log(num))
    num2 = float(input('Type another number '))
    if action == '+':
        action = num + num2
        print(action)
    if action == '-':
        action = num - num2
        print(action)
    if action == '*':
        action = num * num2
        print(action)
    if action == '**':
        action = num ** num2
        print(action)
    if action == '/':
        action = num / num2
        print(action)
    if action == '%':
        action = (num / (num2*10)) * 100
        print('{}%'.format(action))
