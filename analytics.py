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