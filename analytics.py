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
    Fetches and returns the most sold car make.

    :param sales: List data gathered from `load_sales`.
    :return: The most sold car make.
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

        except:  # Malformed entry, ignore, move on.
            continue

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

    car_sales_stats = {}
    for sale in sales:
        try:
            car_make_and_model = f"{sale['make']} {sale['model']}"

            # Add salesperson to dictionary if they don't exist
            if car_make_and_model not in car_sales_stats:
                car_sales_stats[car_make_and_model] = 1
                continue

            car_sales_stats[car_make_and_model] += 1

        except:  # Malformed entry, ignore, move on.
            continue

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
    averaged_sales_person_data = {}

    # Generate the average sales count for every sales person and add it to a dictionary
    for sales_person in sales_person_data:
        sales_person_name        = sales_person
        sales_person_total_value = sales_person_data[sales_person]['total_sale_value']
        sales_person_total_sales = sales_person_data[sales_person]['total_sale_count']

        average_value = round(sales_person_total_value / sales_person_total_sales, 2)

        averaged_sales_person_data[sales_person_name] = average_value

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