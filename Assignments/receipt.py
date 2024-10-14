import csv
KEY_COLUMN_INDEX = 0
def main():
    dictionary = read_dictionary("products.csv", KEY_COLUMN_INDEX)
    print(dictionary)
    with open("request.csv", "rt") as request_file:
        request_list = csv.reader(request_file)
        next(request_file)
        for request in request_list:
            code = request[0]
            quantity = int(request[1])
            if code in dictionary:
                product_info = dictionary[code]
                product_name = product_info[1]
                product_price = float(product_info[2])
                print(f"{product_name}: {quantity} units, ${product_price}")
            else:
                print("Product was not found")



def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file);
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    
    return dictionary
if __name__ == "__main__":
    main()
