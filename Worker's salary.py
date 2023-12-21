worker = dict()
worker['Name'] = str(input('Name: '))
worker['Age'] = 2023 - (int(input('Birth date: ')))
worker['Workcard'] = int(input("Work card (0 = don't have): "))
if worker['Workcard'] == 0:
    print(f"\n{worker['Name']} haven't luck with jobs")
else:
    worker['Year of hiring'] = int(input('Year of hiring: '))
    worker['Salary'] = float(input('Salary: '))
    worker['Retirement'] = worker['Age'] + ((worker['Year of hiring'] + 35) - 2023)
    for n, v in worker.items():
        print(f'{n} --- {v}')
