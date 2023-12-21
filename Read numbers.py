# Tuple
string = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
while True:
    reader = int(input('Type an integer number between 0 and 10\n'))
    if reader > 10:
        print(f"This number '{reader}' isn't between 0 and 10")
    if reader <= 10:
        break
print(f'You typed the number {string[reader]}')
