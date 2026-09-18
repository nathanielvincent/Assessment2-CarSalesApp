# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# The primary handler for calling functions from `analytics.py` as is requested
# by main.py for the terminal interface people interact with

from analytics import *
from global_functions import *

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
        return []

    with open(filename, 'r') as file:
        lines       = file.readlines()
        csv_keys    = lines[0].strip().split(",") # Build the CSV header keys
        car_sales   = []

        for line in lines[1:]:
            car_sales_cache_dict = {} # Set the cache dict here so it gets reset with every run of the loop.
            split_sales_data     = line.strip().split(",") # Split the keys from the line.

            # Ensure the length of the entries matches the key count.
            if len(split_sales_data) != len(csv_keys):
                continue

            for i in range(len(csv_keys)):
                # Convert the data into integers if possible.
                # TODO: Error handling when malformed data
                entry_data = parse_value(split_sales_data[i])

                car_sales_cache_dict[csv_keys[i]] = entry_data # Add the data to the cache dictionary

            car_sales.append(car_sales_cache_dict)  # Add the cache dictionary to the car sales list.

        return car_sales

def grab_analytics(run_option: str, csv_file_path: str) -> None:
    """
    This is the brains of the interaction menu, where all data is fetched,
    and printed. It is done this way so all data can be printed in a human-readable
    way, which requires printing differently per interaction.

    :param run_option: Which sales data to read.
    :param csv_file_path: The file to read data from.
    :return: None.
    """
    sale_data = load_sales(csv_file_path)

    if run_option == 'Total Sales':
        total_sale_count = total_sales(sale_data)
        print(f"There have been a total of {total_sale_count} sales.")


    elif run_option == 'Total Revenue':
        total_revenue_amount = total_revenue(sale_data)
        print(f"The total amount of revenue made from car sales is ${total_revenue_amount:.2f}.")


    elif run_option == 'Sales by Salesperson':
        sales_by_salesperson_data = sales_by_salesperson(sale_data)

        print("Sales Person Sales Statistics!")
        for salesperson in sales_by_salesperson_data:
            sales_count = sales_by_salesperson_data[salesperson]
            sales_count_string = f"{sales_count} sales"

            print(f"{salesperson:<10} {sales_count_string:>10}")


    elif run_option == 'Most Sold Make':
        most_sold_make_data = most_sold_make(sale_data)
        print(f"The most sold car make is {most_sold_make_data}.")


    elif run_option == 'Least Sold Model':
        least_sold_model_data = least_sold_model(sale_data)
        print(f"The least sold car make and model is {least_sold_model_data}.")


    elif run_option == 'Average Sale by Salesperson':
        average_sale_amount = average_sale_by_salesperson(sale_data)
        for salesperson in average_sale_amount:
            sales_average = average_sale_amount[salesperson]
            sales_average_price = f"${sales_average:.2f}"

            print(f"{salesperson:<10} {sales_average_price:>10}")


    elif run_option == 'Top Salesperson by Average':
        top_salesperson = top_salesperson_by_average(sale_data)
        print(f"{top_salesperson} has the highest sale average.")

    elif run_option == 'Sales in Month':
        year  = input("Which year would you like to check? ")
        month = input("Which month would you like to check? (Month Number!) ")

        if year.isdigit() and month.isdigit():
            month_data = sales_in_month(sale_data, year, month)

            # Print human friendly message for "No sales"
            if len(month_data) == 0:
                print(f"There are no recorded sales in {year}-{month}.")

            else:
                print(f"Here's a list of sales made in {year}-{month}:")

                for entry in month_data:
                    salesperson = entry['salesperson']
                    car = f"{entry['make']} {entry['model']}"
                    price = f"${entry['price']:.2f}"

                    print(f"{salesperson} sold a {car} for {price}.")
        else:
            print("\n!! One or more input is incorrect, please try again !!")

    elif run_option == 'Best Month':
        best_month_data = best_month(sale_data)
        print(f"The most profitable month in the dataset is {best_month_data}.")

    # Don't continue until the user is ready
    input("\n[Press enter to continue]")
    clear_terminal()