# Ink efficiency

ww = float(input('Type the width of the object:'))
wh = float(input('Type the height of the object:'))
a = ww * wh
iq1 = (a / 5)
iq2 = (a / 10)
iq3 = (a / 20)
iq4 = (a / 40)
if a < 5:
    print('Area of the object:{:.1f}\nQuantity of gallons of 1L:{:.1f}'.format(a, iq1))
if 10 > a >= 5:
    print('Area of the object:{:.1f}\nQuantity of gallons of 5L:{:.1f}'.format(a, iq2))
if 20 > a >= 10:
    print('Area of the object:{:.1f}\nQuantity of gallons of 10L:{:.1f}'.format(a, iq3))
if 40 > a >= 20:
    print('Area of the object:{:.1f}\nQuantity of gallons of 20L:{:.1f}'.format(a, iq4))
if a > 40:
    print('Area of the object:{:.1f}\nQuantity of gallons of 20L:{:.1f}'.format(a, iq4))
