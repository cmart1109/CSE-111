import math;
pi = math.pi
def main():
    calculate("#1 Picnic", 6.83, 10.16)
    calculate("#1 Tall", 7.78, 11.91)
    calculate("#2", 8.73, 11.59)
    calculate("#2.5", 10.32, 11.91)
    calculate("#3 Cylinder", 10.79, 17.78)
    calculate("#5", 13.02, 14.29)
    calculate("#6Z", 5.40, 8.89)
    calculate("#BZ Short", 6.83, 7.62)
    calculate("#10", 15.72, 17.78)
    calculate("#211", 6.83, 12.38)
    calculate("#300", 7.62, 11.27)
    calculate("#303", 8.10, 11.11)

pass
def calculate(name, radius, height):
        volume = compute_volume(radius, height)
        surface = compute_surface_area(radius, height)
        storage = storage_efficiency(volume, surface)
        storage = round(storage, 2)
        print (f"{name},  {storage}")
def compute_volume(radius, height):
        volume = pi * radius **2 * height
        return volume
def compute_surface_area(radius, height):
        surface_area = 2* pi * radius * (radius + height)
        return surface_area
def storage_efficiency(vol, surface_area):
        se = vol/surface_area
        return se

main();