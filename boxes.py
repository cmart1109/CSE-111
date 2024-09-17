
import math
items = float(input('Enter the number of items: '))
ipb = float(input('Enter the number of items per box: '))

boxes = items/ipb
boxesRounded = math.ceil(boxes)
print(f'For {items:.1f} items, and packing {ipb:.1f} you will need {boxesRounded:.0f} Boxes')