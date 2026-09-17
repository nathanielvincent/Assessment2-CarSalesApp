from main import load_sales
from analytics import *

def grab_analytics(run_option: str) -> None:
    sale_data = load_sales('./car_sales.csv')