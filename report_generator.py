# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# Generates a report of all the information from `analytics.py` and saves it to a text file.

from analytics import *
from analytics_grabber import load_sales

from constants import *

import uuid
from pathlib import Path

def write_report(sales: list, filename: str) -> None:
    """
    Writes a report file with the information from analytics.py

    :param sales: List data gathered from `load_sales`.
    :param filename: The output path to save the report to.
    :return: Nothing.
    """

    total_sales_amount      = total_sales(sales)
    total_revenue_amount    = total_revenue(sales)
    sales_per_salesperson   = sales_by_salesperson(sales)

    most_sold_car_make      = most_sold_make(sales)
    least_sold_car_model    = least_sold_model(sales)

    average_salesperson_sales   = average_sale_by_salesperson(sales)
    top_salesperson_average     = top_salesperson_by_average(sales)

    with open(filename, 'w') as file:
        # General Stats ---------------------------
        file.write(f'VEHICLE SALES STATS:\n')
        file.write(f'Total car sales in the dataset       - {total_sales_amount}\n')
        file.write(f'Total Revenue from all sales         - ${total_revenue_amount:.2f}\n\n')
        file.write(f'The overall most sold vehicle make   - {most_sold_car_make}.\n')
        file.write(f'The overall least sold vehicle model - {least_sold_car_model}.\n\n\n')

        # Total sale count ---------------------------
        file.write(f'SALES PEOPLE STATS:\n')
        file.write(f'The top sales person based on average sales price is {top_salesperson_average}.\n\n\n')

        file.write('Total Sales Amount Per Sales Person\n\n')
        file.write(f"{'Name':<10}{'Total Sales':>15}\n")
        file.write('-' * 30 + '\n') # Add a gap
        for name, value in sales_per_salesperson.items():
            file.write(f"{name:<10}{value:>10}\n")

        # Average sale amount ---------------------------
        file.write('\n\n\nAverage Sales Amount Per Sales Person\n\n') # Put a small gap between tables
        file.write(f"{'Name':<10}{'Average Sale Amount':>15}\n")
        file.write('-' * 30 + '\n') # Add a gap
        for name, value in average_salesperson_sales.items():
            sales_value = f"${value:.2f}" # Convert to dollars
            file.write(f"{name:<10}{sales_value:>15}\n")

    print(f"Report successfully written to {report_path}!")

if __name__ == "__main__":
    # Custom ID for every report, don't overwrite old ones.
    report_path = f"./report_{uuid.uuid4()}.txt"
    sale_data = load_sales(WORKING_DATA_FILE)

    write_report(sale_data, report_path)