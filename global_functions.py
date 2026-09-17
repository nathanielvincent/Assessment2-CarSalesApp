import os

def clear_terminal():
    """
    Clears the terminal screen, for readability

    :return: None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

