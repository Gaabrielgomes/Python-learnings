# The 1% challenge
import random
import emoji
num = random.randint(1, 100)
answer = int(input('Try to guess the selected number: '))
c = 0
while answer != num:
    answer = int(input('Wrong guess, haha!\nTry again: '))
    num = random.randint(1, 100)
    c += 1
    if c % 10 == 0:
        print("Wrong answer!")
        answer1 = str(input('Wanna continue trying? [y/n] '))
        if answer1 == 'y':
            answer = int(input('Ok, so try to hit the correct number\nCorrect number: '))
        else:
            print(emoji.emojize('\n\nYou succumbed by the power of a simple code, haha!:smiling_face_with_horns:\n\n'))
        break
if answer == num:
    print('Ur lucky. We have a winner!')
