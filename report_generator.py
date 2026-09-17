from analytics import *
from analytics_grabber import load_sales
import uuid

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
        file.write(f'Total car sales in the dataset - {total_sales_amount}\n')
        file.write(f'Total Revenue from all sales - ${total_revenue_amount:.2f}\n\n')
        file.write(f'{sales_per_salesperson}\n\n')
        file.write(f'The overall most sold vehicle make: {most_sold_car_make}.\n')
        file.write(f'The overall least sold vehicle model: {least_sold_car_model}.\n\n')
        file.write(f'{average_salesperson_sales}\n')
        file.write(f'{top_salesperson_average}\n')

    print(f"Report successfully written to {report_path}!")

if __name__ == "__main__":
    # Custom ID for every report, don't overwrite old ones.
    report_path = f"./report_{uuid.uuid4()}.txt"
    sale_data = load_sales('./car_sales.csv')

    write_report(sale_data, report_path)