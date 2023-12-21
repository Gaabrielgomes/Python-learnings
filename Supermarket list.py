print('{:~^30}'.format("Gabriel's Market"))
counter = total = expensive = cheapest = 0
quest = str
cheapn = ()
while quest != 'n':
    print('{:~^30}'.format('Add any product'))
    name = input('Name of the product ')
    price = float(input('Price: '))
    counter += 1
    total += price
    if price < cheapest or counter == 1:
        cheapn = name
        cheapest = price
    if price > 100:
        expensive += 1
    quest = input('Wanna add something?[enter/n]')
print(f'The total in your cart is ${total:.2f}.\n'
      f'You have {expensive} expensive items.\n'
      f'The cheapest product is {cheapn}, that costs ${cheapest}')
