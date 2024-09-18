import datetime
date = datetime.datetime.now().weekday()
subTotal = float(input('Please Enter the SubTotal: '))
if date == 1 or date == 2:
    if subTotal >= 50:
        taxes = subTotal*0.06
        total = subTotal*0.9 + taxes
        print(f'Sales tax Amount: {taxes}')
        print('Because you are purchasing more than $50, you gain a 10% Discount!')
        print(f'The Total is {total}')
    else:
        taxes = subTotal*0.06
        total = subTotal + taxes
        print(f'Sales tax Amount: {taxes}')
        print(f'The Total is {total}')
else:
        taxes = subTotal*0.06
        total = subTotal + taxes
        print(f'Sales tax Amount: {taxes}')
        print(f'The Total is {total}')