import math;
pi = math.pi
def main():
    #volume = compute_volume(6.83, 10.16)
    #surface_area = compute_surface_area
    Picnic = storage_efficiency(compute_volume(6.83, 10.16), compute_surface_area(6.83, 10.16))
    print(f'#1 Picnic {Picnic}')
pass
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