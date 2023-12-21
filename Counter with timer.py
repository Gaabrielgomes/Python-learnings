import time
term = int(input('Tell the first term: '))
reason = int(input('Tell the reason: '))
counter = 0
while counter != 10:
    term += reason
    counter += 1
    time.sleep(1)
    print(term)
repeater = float
while repeater != 'n':
    repeater = input('Wanna print more terms? ')
    counter2 = 0
    if repeater == 'y':
        cont = int(input('How many do you want? '))
        while counter2 != cont:
            term += reason
            counter2 += 1
            time.sleep(1)
            print(term)
    else:
        print('\n\nThe code ended')
