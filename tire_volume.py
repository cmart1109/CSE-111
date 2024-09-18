# Tire Volume Calculator
import math;

w = float(input('Please enter the width of the tire in mm (ex 205): '))
a = float(input('Please Enter the aspect ratio of the tire (ex 60): '))
d = float(input('Please Enter the diameter of the wheel in inches (ex 15): '))

pi = math.pi
v = (pi*(w**2)*a*(w*a+2540*d))/10000000000
volume = round(v, 2)
print(f'The Approximate volume is {volume} Liters')