# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# Constant variables and functions that multiple files depend on, so they're here instead
# of being duplicated multiple times through the source.

import os
from pathlib import Path

# This is the file that will be utilised by the code for all functions.
# If you wish to change the file it reads, change this, and everything will use it.
WORKING_DIR = Path(__file__).resolve().parent
WORKING_DATA_FILE = WORKING_DIR / 'Data' / 'car_sales.csv'

# Options that will appear on startup for the interaction menu in main.py.
# This is also used for analytics_grabber.py to know what code to run.
MENU_OPTIONS_LIST = [
    "Total Sales",
    "Total Revenue",
    "Sales by Salesperson",
    "Most Sold Make",
    "Least Sold Model",
    "Average Sale by Salesperson",
    "Top Salesperson by Average",
    "Sales in Month",
    "Best Month",
    "Quit",
]

def clear_terminal():
    """
    Clears the terminal screen, for readability

    :return: None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')