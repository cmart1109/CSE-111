import csv
from datetime import datetime, timedelta
current_day_and_time = datetime.now()
KEY_COLUMN_INDEX = 0


def main(): 
    try:
        subtotal_amount = 0
        total_items = 0
        dictionary = read_dictionary("products.csv", KEY_COLUMN_INDEX)
        print("Christian's Market")
        with open("request.csv", "rt") as request_file:
            request_list = csv.reader(request_file)
            next(request_file)
            for request in request_list:
                code = request[0]
                quantity = int(request[1])
                try:
                    product_info = dictionary[code]
                except KeyError as key_err:
                    print("Error: unknown product ID in the request.csv file")
                    print(f"{key_err}")
                    return
                product_price = float(product_info[2])
                product_name = product_info[1]
                total_price = product_price * quantity
                total_items += quantity
                subtotal_amount += total_price 
                print(f"{product_name}: {quantity} @ ${product_price}")

        subtotal_amount = round(subtotal_amount, 2)
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal_amount}")
        sales_tax = round(subtotal_amount * 0.06, 2)
        print(f"Sales Tax: {sales_tax}") 
        total = subtotal_amount + sales_tax
        total = round(total, 2)
        print(f"Total: {total}")
        print("Thank you for shopping at the Christian's Market")
        print(f"{current_day_and_time: %A %I %M %p}, {current_day_and_time}")

# Exceeding the Requirements -------------------------------------------------------------------------
        new_year = datetime(current_day_and_time.year + 1, 1, 1)
        days_until_new_years_eve = (new_year - current_day_and_time).days
        print(f"Days until New Year's sale: {days_until_new_years_eve}")

        return_by_date = current_day_and_time + timedelta(days=30)
        return_by_time = return_by_date.replace(hour=21, minute=0, second=0, microsecond=0)
        print(f"Return by {return_by_time: %A, %B %d, %Y at %I: %M %p}")
# ----------------------------------------------------------------------------------------------------
    except FileNotFoundError as file_err:
        print("Error: Missing File")
        print(f"{file_err}")
        return
    
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
