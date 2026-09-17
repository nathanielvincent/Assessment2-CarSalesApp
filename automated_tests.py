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