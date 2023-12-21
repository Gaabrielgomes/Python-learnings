gender = str
while gender != 'm' or gender != 'f':
    gender = str(input('Tell your gender: '))
    if gender == 'm':
        print('You are a man')
        break
    if gender == 'f':
        print('You are a woman')
        break
    if gender != 'm' or 'f':
        print('You are not a/an {}'.format(gender))
        print('This code only accept the original genders')
