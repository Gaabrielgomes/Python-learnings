#Salary
sal = float(input('How much do you earn monthly?'))
nsal = sal + (sal*(15/100))
print('Old salary:', sal)
print('New salary:{:.2f}'.format(nsal))
