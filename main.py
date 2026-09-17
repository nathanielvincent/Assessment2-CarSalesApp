# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A program to read car sale data from a .csv

import os
from analytics import *

# Options that will appear on startup for the interaction menu.
MENU_OPTIONS = {
    "Total Sales": "total_sales",
    "Total Revenue": "total_revenue",
    "Sales by Salesperson": "sales_by_salesperson",
    "Most Sold Make": "most_sold_make",
    "Least Sold Model": "least_sold_model",
    "Quit": "quit"
}

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

def sales_interaction_menu() -> None:
    """
    Runs a menu of data analysis options until the user requests a quit.

    :return:
    """

    option_index_match = {}
    user_request_exit = False

    while not user_request_exit:
        # Dynamically print menu options based on the coded options.
        for index, option in enumerate(MENU_OPTIONS, start=1):
            print(f"{index}. {option}")
            option_index_match[str(index)] = option

        selected_option = input("\nWhich option would you like to view? (Use the numbers!) ").lower().strip()

        # Fetch the menu option to run
        if selected_option in option_index_match:
            option_index = option_index_match[selected_option]
            run_option = MENU_OPTIONS[option_index]

            # Quit when the user asks.
            if run_option == 'quit':
                user_request_exit = True

            else:
                grab_analytics(run_option)

        else:
            print("\n\n!! That is not a valid option, please try again !!\n\n")


if __name__ == '__main__':
    sales_interaction_menu()

    # sale_data = load_sales('./car_sales.csv')
    #
    # least_sold  = least_sold_model(sale_data)
    # most_sold   = most_sold_make(sale_data)
    # sales_count = total_sales(sale_data)
    # revenue     = total_revenue(sale_data)
    #
    # print(f"Least Sold Model: {least_sold}")
    # print(f"Most Sold Make  : {most_sold}")
    # print(f"Total Sales     : {sales_count}")
    # print(f"Total Revenue   : {revenue}")