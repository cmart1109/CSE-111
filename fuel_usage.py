import math;

def main():
    start = int(input("Please enter the first odometer reading (miles): "))
    end = int(input("Please enter the second odometer reading (miles): "))
    galloons = float(input("Enter the amount of fuel used (galloons): "))

    milespg = miles_per_galloon(start, end, galloons)
    milespg = math.ceil(milespg)
    print(f'{milespg} Miles per galloon')

    lp100k = lp100k_from_mpg(milespg)
    lp100k = math.ceil(lp100k)
    print(f'{lp100k} Liters per 100 kilometers')

pass
def miles_per_galloon(e, s, g):
        milesPerGalloon = (e - s) / g
        return milesPerGalloon

def lp100k_from_mpg(mpg):
        liters =  (235.215)/mpg
        return liters


main();