# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A file with functions that multiple different sources need,
# to prevent duplication of the same function multiple times.

import os

def clear_terminal():
    """
    Clears the terminal screen, for readability

    :return: None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

