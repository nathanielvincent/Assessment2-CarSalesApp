from main import load_sales
from analytics import *

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
        print(f"There have been a total of {total_sale_count}")