# WATER PRESSURE PROGRAM--------------------------------------------------------------------------
#FUNCTIONS ---------------------------------------------------------------------------------------
earth_gravity = 9.8066500
water_density = 998.2000000
water_dynamic_viscosity = 0.0010016

def water_column_height(tower_height, tank_height):
    h = tower_height + ((3*tank_height)/4)     
    return h

def pressure_gain_from_water_height(height):
    p = (water_density * earth_gravity * height)/1000
    return p

def pressure_loss_from_pipe(pd, pl, ff, fv):
    P = (-ff * pl * water_density * (fv**2))/(2000 * pd)
    return P

def pressure_loss_from_fittings(fv, qf):
    p = (-0.04 * water_density * (fv ** 2) * qf)/2000
    return p

def reynolds_number(hd, fv):
    r = (water_density * hd * fv)/(water_dynamic_viscosity)
    return r

def pressure_loss_from_pipe_reduction(ld, fv, rn, sd):
    k = (0.1 + (50/rn)) * (((ld/sd)**4) - 1)
    p = (-k * water_density * (fv**2))/2000
    return p

def pounds_per_square_inch(kpa):
    psi = kpa / 6.895
    return psi
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    psi = pounds_per_square_inch(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi} pounds per square inch")
if __name__ == "__main__":
    main()

# END ---------------------------------------------------------------------------------------------