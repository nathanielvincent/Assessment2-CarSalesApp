# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A program to read car sale data from a .csv

import os
from analytics import *
from analytics_grabber import grab_analytics

# Options that will appear on startup for the interaction menu.
MENU_OPTIONS = {
    "Total Sales": "total_sales",
    "Total Revenue": "total_revenue",
    "Sales by Salesperson": "sales_by_salesperson",
    "Most Sold Make": "most_sold_make",
    "Least Sold Model": "least_sold_model",
    "Quit": "quit"
}

def sales_interaction_menu() -> None:
    """
    Runs a menu of data analysis options until the user requests a quit.

    :return:
    """

    option_index_match = {}
    user_request_exit = False

    while not user_request_exit:
        # Dynamically print menu options based on the coded options.
        for index, option in enumerate(MENU_OPTIONS, start=1):
            print(f"{index}. {option}")
            option_index_match[str(index)] = option

        selected_option = input("\nWhich option would you like to view? (Use the numbers!) ").lower().strip()

        # Fetch the menu option to run
        if selected_option in option_index_match:
            option_index = option_index_match[selected_option]
            run_option = MENU_OPTIONS[option_index]

            # Quit when the user asks.
            if run_option == 'quit':
                user_request_exit = True

            else:
                grab_analytics(run_option)

        else:
            print("\n\n!! That is not a valid option, please try again !!\n\n")


if __name__ == '__main__':
    sales_interaction_menu()