# Tire Volume Calculator
import datetime;
import math;
# Inputs
w = int(input('Please enter the width of the tire in mm (ex 205): '))
a = int(input('Please Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Please Enter the diameter of the wheel in inches (ex 15): '))
# Round Numbers
w = math.ceil(w)
a = math.ceil(a)
d = math.ceil(d)
pi = math.pi
# Operation
v = (pi*(w**2)*a*(w*a+2540*d))/10000000000
volume = round(v, 2)
print(f'The Approximate volume is {volume} Liters')
today = datetime.datetime.now()
print('Would you like to buy tires with the size that you requested with us?')
print('1.- YES   2.- NO')

while True:
    buyer = int(input(''))
    if buyer == 1:
        # ask for the phone number
        phone = int(input('Please enter your phone number to call you back for more details: '))
        phone = math.ceil(phone)
        # Write on the TXT file 
        with open('volumes.txt', 'a') as file: 
            file.write(f'{today:%Y-%m-%d}, ')
            file.write(f'{w}, ')
            file.write(f'{a}, ')
            file.write(f'{d}, ')
            file.write(f'{volume}, ')
            file.write(f'{phone}.')
            file.write('\n')
            print('The phone number was succesfully registered')
            print('Thank you for choosing us as your personal Volume calculator :)')
            break
    elif buyer == 2: 
        # Write on the TXT file 
        with open('volumes.txt', 'a') as file: 
            file.write(f'{today:%Y-%m-%d}, ')
            file.write(f'{w}, ')
            file.write(f'{a}, ')
            file.write(f'{d}, ')
            file.write(f'{volume}.')
            file.write('\n')
            print('Thank you for choosing us as your personal Volume calculator :)')
            break
    else:
        print('Please enter a valid Option')
    





