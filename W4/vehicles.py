def main():

    vehicles_dict = {
        
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }

    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3
    vin = input("Please enter a VIN: ")
    if vin in vehicles_dict:

        car = vehicles_dict[vin]
        manufacturer = car[MANUFACTURER_INDEX]
        model = car[MODEL_INDEX]
        color = car[COLOR_INDEX]
        print(f"The manufacturer is {manufacturer}, the model is {model}, and is color {color}")

    else:
        (f"{vin} is not in the dictionary.")

if __name__ == "__main__":
    main()
