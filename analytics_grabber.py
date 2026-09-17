from analytics import *
import os

def parse_value(value):
    """
    Parses the given value and will convert it to an int, float, or just return the normal value

    :param value: data to check the type.
    :return: modified data, either an int, float, or value.
    """

    if value.isdecimal():
        return int(value)

    try:
        return float(value)

    except ValueError:
        return value

def load_sales(filename: str) -> list:
    """
    Loads all sales information from the provided file path and returns a list
    with formatted data entries using respective key headers.

    :param filename: the path to the sales data csv.
    :return: a list of dictionaries with sales data.
    """

    if not os.path.exists(filename):
        # Don't throw python errors at the user, handle errors safely.
        print('Sales data file path does not exist.')
        return

    with open(filename, 'r') as file:
        lines       = file.readlines()
        csv_keys    = lines[0].strip().split(",") # Build the CSV header keys
        car_sales   = []

        for line in lines[1:]:
            car_sales_cache_dict = {} # Set the cache dict here so it gets reset with every run of the loop.
            split_sales_data     = line.strip().split(",") # Split the keys from the line.

            for i in range(len(csv_keys)):
                # Convert the data into integers if possible.
                # TODO: Error handling when malformed data
                entry_data = parse_value(split_sales_data[i])

                car_sales_cache_dict[csv_keys[i]] = entry_data # Add the data to the cache dictionary

            car_sales.append(car_sales_cache_dict)  # Add the cache dictionary to the car sales list.

        return car_sales

def grab_analytics(run_option: str) -> None:
    """
    This is the brains of the interaction menu, where all data is fetched,
    and printed. It is done this way so all data can be printed in a human-readable
    way, which requires printing differently per interaction.

    :param run_option: which sales data to read.
    :return:
    """
    sale_data = load_sales('./car_sales.csv')

    if run_option == 'total_sales':
        total_sale_count = total_sales(sale_data)
        print(f"There have been a total of {total_sale_count} sales.")

    elif run_option == 'total_revenue':
        total_revenue_amount = total_revenue(sale_data)
        print(f"The total amount of revenue made from car sales is ${total_revenue_amount:.2f}.")

    elif run_option == 'sales_by_salesperson':
        sales_by_salesperson_data = sales_by_salesperson(sale_data)

        print("Sales Person Sales Statistics!")
        for salesperson in sales_by_salesperson_data:
            sales_count = sales_by_salesperson_data[salesperson]
            print(f"{salesperson} - {sales_count} sales!")

    # Don't continue until the user is ready
    input("\n[Press enter to continue]")