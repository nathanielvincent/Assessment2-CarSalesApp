# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# Code to handle automatated testing to ensure functions are running as expected.

import pytest
from analytics import *

TEST_DATA = [
    {'sale_id': 10000, 'date': '2026-06-11', 'salesperson': 'Ben', 'make': 'Tesla', 'model': 'Model 3', 'year': 2024, 'price': 58000.0},
    {'sale_id': 10001, 'date': '2026-10-05', 'salesperson': 'Emily', 'make': 'Subaru', 'model': 'i-dont-know-cars', 'year': 1903, 'price': 16000.0},
    {'sale_id': 10002, 'date': '2026-06-21', 'salesperson': 'Mark', 'make': 'Honda', 'model': 'Civic', 'year': 2006, 'price': 12000.0},
    {'sale_id': 10003, 'date': '2026-12-31', 'salesperson': 'Ben', 'make': 'Honda', 'model': 'Civic', 'year': 2006, 'price': 12000.0},
    {'sale_id': 10004, 'date': '2026-01-30', 'salesperson': 'Joe', 'make': 'Volkswagen', 'model': 'Polo', 'year': 1980, 'price': 8000.0}
]

def test_total_sales():
    # There are 5 total entries in test data, so it should return 5.
    assert total_sales(TEST_DATA) == 5

def test_total_revenue():
    # Sum of all test data sales is 106,000. Data is returned from the function without
    # commas, and with two decimal places, thus it should return `106000.00`
    assert total_revenue(TEST_DATA) == 106000.00

def test_sales_by_salesperson():
    # Ben sells two vehicles, everyone else sells one. The output should return Ben.
    expected_result = {
        "Ben": 2,
        "Emily": 1,
        "Mark": 1,
        "Joe": 1
    }
    assert sales_by_salesperson(TEST_DATA) == expected_result

def test_most_sold_make():
    # Two instances of Honda in test data, only one instance of other brands.
    assert most_sold_make(TEST_DATA) == "Honda"

def test_least_sold_model():
    # Dataset is too small to have a "Least sold vehicle" but the Tesla Model 3 is only
    # sold one time, and it appears first in the list, so the function will return Tesla Model 3.
    assert least_sold_model(TEST_DATA) == 'Tesla Model 3'

def test_fetch_salesperson_data():
    expected_result = {
        "Ben": {'total_sale_value': 70000.0, 'total_sale_count': 2}, # Ben sells two vehicles, one at 58k, one at 12k. Result is 70k, 2 cars
        "Emily": {'total_sale_value': 16000.0, 'total_sale_count': 1}, # Emily sells one vehicle at 16k. Result is 16k, 1 car
        "Mark": {'total_sale_value': 12000.0, 'total_sale_count': 1}, # Mark sells one vehicle at 12k. Result is 12k, 1 car
        "Joe": {'total_sale_value': 8000.0, 'total_sale_count': 1}, # Joe sells one vehicle at 8k. Result is 8k, 1 car
    }
    assert fetch_salesperson_data(TEST_DATA) == expected_result

def test_average_sale_by_salesperson():
    expected_result = {
        "Ben": 35000.0, # Ben sells two vehicles, one at 58k, one at 12k. Result is 70k. Averaged makes it 35k.
        "Emily": 16000.0, # Emily only sells one vehicle, average shouldn't change
        "Mark": 12000.0, # Mark only sells one vehicle, average shouldn't change
        "Joe": 8000.0, # Joe only sells one vehicle, average shouldn't change
    }
    assert average_sale_by_salesperson(TEST_DATA) == expected_result

def test_top_salesperson_by_average():
    # Ben sells two vehicles, one at 58k, one at 12k. Result is 70k,
    # averaged between 2 vehicles this is 35k per vehicle, higher than anyone else.
    assert top_salesperson_by_average(TEST_DATA) == 'Ben'

# Sales in month testing ---------------------------------------------------
def test_sales_in_month_one():
    # These are the only two sales in 2026-06, they should be all that is returned.
    expected_result = [
        {'sale_id': 10000, 'date': '2026-06-11', 'salesperson': 'Ben', 'make': 'Tesla', 'model': 'Model 3', 'year': 2024, 'price': 58000.0},
        {'sale_id': 10002, 'date': '2026-06-21', 'salesperson': 'Mark', 'make': 'Honda', 'model': 'Civic', 'year': 2006, 'price': 12000.0},
    ]
    assert sales_in_month(TEST_DATA, "2026", "06") == expected_result

def test_sales_in_month_two():
    # There are no sales in 2025 at all, so it should return nothing.
    expected_result = []
    assert sales_in_month(TEST_DATA, "2025", "06") == expected_result