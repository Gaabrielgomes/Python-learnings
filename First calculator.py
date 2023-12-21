# Aritmetical operations
n1 = int(input('Number 1:'))
n2 = int(input('Number 2:'))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
p = n1 ** n2
m = n1 * n2
di = n1 // n2
redi = n1 % n2
print('Sum:{}\nSubtraction:{}\nDivision:{:.2f}\nMultiplication:{}'.format(s, sub, d, m))
print('Power:{}\nInteger division:{}\nRest of division:{}'.format(p, di, redi))
