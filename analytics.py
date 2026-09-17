# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# Functions to fetch analytics from provided car sales stats

def validate_sale(sale: dict) -> bool:
    """
    Validates a sale entry, checks for any malformed entries and will return data accordingly

    :param sale: One sale entry gathered from `load_sales`.
    :return: Will return True if entry is okay, otherwise False.
    """

    # Check for missing keys
    check_keys = ['sale_id', 'date', 'salesperson', 'make', 'model', 'year', 'price']
    for key in check_keys:
        if key not in sale:
            return False

    # Check for empty keys
    for key in sale:
        if not sale[key]:
            return False

    return True

def total_sales(sales: list) -> int:
    """
    Returns the total count of sales from the provided data.

    :param sales: List data gathered from `load_sales`.
    :return: Integer count of sales.
    """

    total_sale_count = 0
    for sale in sales:
        # Check to ensure no malformed entries before adding to list.
        if validate_sale(sale):
            total_sale_count += 1

    return total_sale_count


def total_revenue(sales: list) -> float:
    """
    Returns the total revenue from sales.

    :param sales: List data gathered from `load_sales`.
    :return: Float of total revenue count.
    """

    revenue_total = 0
    for sale in sales:
        # Check to ensure no malformed entries before adding to list.
        if validate_sale(sale):
            try:
                price = sale['price']
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
        # Check to ensure no malformed entries before adding to list.
        if validate_sale(sale):
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


def build_car_sales_stats_dict(sales: list) -> dict:
    """

    :param sales: List data gathered from `load_sales`.
    :return:
    """

    car_sales_stats = {}
    for sale in sales:
        # Check to ensure no malformed entries before adding to list.
        if validate_sale(sale):
            try:
                car_make_and_model = f"{sale['make']} {sale['model']}"

                # Add salesperson to dictionary if they don't exist
                if car_make_and_model not in car_sales_stats:
                    car_sales_stats[car_make_and_model] = 1
                    continue

                car_sales_stats[car_make_and_model] += 1

            except:  # Malformed entry, ignore, move on.
                continue

    return car_sales_stats


def most_sold_make(sales: list) -> str:
    """
    Fetches and returns the most sold car make.

    :param sales: List data gathered from `load_sales`.
    :return: The most sold car make.
    """

    car_sales_stats = build_car_sales_stats_dict(sales)

    most_sold_make_count = 0
    best_sold_make       = ""
    for make in car_sales_stats:
        # Check if car make sales is more than already stored most sold count
        if car_sales_stats[make] > most_sold_make_count:
            most_sold_make_count = car_sales_stats[make]
            best_sold_make = make

    return best_sold_make

def least_sold_model(sales: list) -> str:
    """
    Fetches and returns the least sold car make and model.

    :param sales: List data gathered from `load_sales`.
    :return: The least sold car make and model.
    """

    car_sales_stats = build_car_sales_stats_dict(sales)

    # This is honeslty *garbage*. I'll rework it.
    lowest_sales        = 0
    lowest_sold_model   = ""
    for car_model in car_sales_stats:
        car_sales = car_sales_stats[car_model]

        if lowest_sales == 0:
            lowest_sales      = car_sales
            lowest_sold_model = car_model
            continue

        if car_sales < lowest_sales:
            lowest_sales      = car_sales
            lowest_sold_model = car_model

    return lowest_sold_model


def fetch_salesperson_data(sales: list) -> dict:
    """
    Takes the provided sales data and generates the amount of sales each salesperson has made,
    and the total value of all of those sales.

    :param sales: List data gathered from `load_sales`.
    :return: a dictionary of salespeople, their total sale count, and total sale value.
    """

    sales_person_data = {}
    for sale in sales:
        # Check to ensure no malformed entries before adding to list.
        if validate_sale(sale):
            salesperson = sale['salesperson']
            sale_value = sale['price']

            # Add the sales person to the dictionary if they're not in it already.
            if salesperson not in sales_person_data:
                sales_person_data[salesperson] = {'total_sale_value': sale_value, 'total_sale_count': 1}
                continue

            # Add the data to the sales persons stats if they're already in the dictionary.
            sales_person_data[salesperson]['total_sale_count'] += 1
            sales_person_data[salesperson]['total_sale_value'] += sale_value

    return sales_person_data


def average_salesperson_data(sales_person_data: dict) -> dict:
    """
    Generates the average of every salespersons sales as is gathered from `fetch_salesperson_data`.

    :param sales_person_data: List data gathered from `fetch_salesperson_data`.
    :return: A dictionary of sales people names and their averaged sales values.
    """

    # Generate the average sales count for every sales person and add it to a dictionary
    averaged_sales_person_data = {}
    for sales_person in sales_person_data:
        sales_person_name        = sales_person
        sales_person_total_value = sales_person_data[sales_person]['total_sale_value']
        sales_person_total_sales = sales_person_data[sales_person]['total_sale_count']

        average_value = round(sales_person_total_value / sales_person_total_sales, 2)

        averaged_sales_person_data[sales_person_name] = average_value

    return averaged_sales_person_data


def average_sale_by_salesperson(sales: list) -> dict:
    """
    Fetches the average sale amount of every salesperson in the provided data.

    :param sales: List data gathered from `load_sales`.
    :return: a dictionary keyed with each salesperson name and their average sale amount.
    """

    # I'm too lazy to check the code against an empty list.
    # enjoy this dedicated check.
    if len(sales) == 0:
        return {}

    sales_person_data = fetch_salesperson_data(sales)
    averaged_sales_person_data = average_salesperson_data(sales_person_data)

    return averaged_sales_person_data


def top_salesperson_by_average(sales: list) -> str:
    """
    Takes sales data and finds the salesperson with the highest average sale price.

    :param sales: List data gathered from `load_sales`.
    :return: the salesperson name as a plain string.
    """

    # I'm too lazy to check the code against an empty list.
    # enjoy this dedicated check.
    if len(sales) == 0:
        return "Nobody - Empty list provided!"

    sales_person_data = fetch_salesperson_data(sales)
    averaged_sales_person_data = average_salesperson_data(sales_person_data)

    top_salesperson = ""
    top_salesperson_amount = 0

    for sales_person in averaged_sales_person_data:
        if averaged_sales_person_data[sales_person] > top_salesperson_amount:
            top_salesperson = sales_person
            top_salesperson_amount = averaged_sales_person_data[sales_person]

    return top_salesperson


def sales_in_month(sales: list, year: int | str, month: int | str) -> list:
    """
    Fetches a list of all sales in a specified year and month, then returns them.

    :param sales: List data gathered from `load_sales`.
    :param year: The year (e.g. 2026) to fetch the data from.
    :param month: The month (number, e.g. 5 for May) to fetch the data from.
    :return: A list of all sales made in that month.
    """

    # I'm too lazy to check the code against an empty list.
    # enjoy this dedicated check.
    if len(sales) == 0:
        return []

    sales_date  = f"{year}-{month}"
    sales_made  = []

    for sale in sales:
        # Check to ensure no malformed entries before adding to list.
        if validate_sale(sale):
            if sales_date in sale['date']:
                sales_made.append(sale)

    return sales_made