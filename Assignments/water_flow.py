def main():
    print("cheese")
pass
def water_column_height(tower_height, tank_height):
    h = tower_height + ((3*tank_height)/4)     
    return h

def pressure_gain_from_water_height(height):
    p = (998.2 * 9.80665 * height)/1000
    return p

def pressure_loss_from_pipe(pd, pl, ff, fv):
    P = (-ff * pl * 998.2 * (fv**2))/(2000 * pd)
    return P


main()