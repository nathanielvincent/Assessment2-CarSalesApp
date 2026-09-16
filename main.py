# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A program to read car sale data from a .csv

import os

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
                # TODO: Price to float.
                # TODO: Error handling when malformed data
                entry_data = int(split_sales_data[i]) if split_sales_data[i].isdecimal() else split_sales_data[i]

                car_sales_cache_dict[csv_keys[i]] = entry_data # Add the data to the cache dictionary

            car_sales.append(car_sales_cache_dict)  # Add the cache dictionary to the car sales list.


        return car_sales

if __name__ == '__main__':
    data = load_sales('./car_sales.csv')
    print(data)