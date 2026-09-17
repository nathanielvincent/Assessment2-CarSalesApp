# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A program to read car sale data from a .csv

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


# ANALYTICS FUNCTIONS --------------------------------------------------------
def total_sales(sales: list) -> int:
    """
    Returns the total count of sales from the provided data.

    :param sales: List data gathered from `load_sales`.
    :return: Integer count of sales.
    """
    return len(sales)

def total_revenue(sales: list) -> float:
    """
    Returns the total revenue from sales.

    :param sales: List data gathered from `load_sales`.
    :return: Float of total revenue count.
    """

    revenue_total = 0
    for item in sales:
        try:
            price = item['price']
            revenue_total += price

        except: # Malformed entry, ignore, move on.
            continue

    return float(revenue_total)


def sales_by_salesperson(sales: list) -> dict:
    """
    Generates a dictionary of sales person sales stats

    :param sales: List data gathered from `load_sales`.
    :return: a dictionary of all salespeople and how many sales they have made.
    """

    sales_person_stats = {}
    for sale in sales:
        try:
            sales_person = sale['salesperson']

            # Add salesperson to dictionary if they don't exist
            if sales_person not in sales_person_stats:
                sales_person_stats[sales_person] = 1
                continue

            sales_person_stats[sales_person] += 1

        except: # Malformed entry, ignore, move on.
            continue

    return sales_person_stats

def most_sold_make(sales: list) -> str:
    """

    :param sales: List data gathered from `load_sales`.
    :return:
    """

    car_sales_stats = {}
    for sale in sales:
        try:
            car_make = sale['make']

            # Add salesperson to dictionary if they don't exist
            if car_make not in car_sales_stats:
                car_sales_stats[car_make] = 1
                continue

            car_sales_stats[car_make] += 1

        except: # Malformed entry, ignore, move on.
            continue

    most_sold_make_count = 0
    best_sold_make       = ""
    for make in car_sales_stats:
        # Check if car make sales is more than already stored most sold count
        if car_sales_stats[make] > most_sold_make_count:
            most_sold_make_count = car_sales_stats[make]
            best_sold_make = make

    return best_sold_make


# LOADING DATA --------------------------------------------------------
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

if __name__ == '__main__':
    sale_data = load_sales('./car_sales.csv')
    most_sold_make(sale_data)

    sales_count = total_sales(sale_data)
    revenue = total_revenue(sale_data)

    print(f"Total Sales     : {sales_count}")
    print(f"Total Revenue   : {revenue}")