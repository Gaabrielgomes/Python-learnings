# Approved or Reproved
dic = dict()
dic['name'] = str(input('Name: '))
dic['grade'] = float(input('Grade: '))
if dic['grade'] >= 7:
    dic['sit'] = 'AP'
    for k, v in dic.items():
        print(f'{k} = {v}')
    print(f"Congrats, {dic['name']}!")
else:
    dic['sit'] = 'RP'
    for k, v in dic.items():
        print(f'{k} = {v}')
    print(f"You must study more, {dic['name']}")
