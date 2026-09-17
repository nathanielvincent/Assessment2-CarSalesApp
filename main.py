# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A program to read car sale data from a .csv

from analytics_grabber import grab_analytics
from constants import *

def sales_interaction_menu() -> None:
    """
    Runs a menu of data analysis options until the user requests a quit.

    :return: Nothing.
    """

    option_index_match = {}
    user_request_exit = False

    while not user_request_exit:
        # Dynamically print menu options based on the coded options.
        for index, option in enumerate(MENU_OPTIONS_LIST, start=1):
            print(f"{index}. {option}")
            option_index_match[str(index)] = option

        selected_option = input("\nWhich option would you like to view? (Use the numbers!) ").lower().strip()

        # Fetch the menu option to run
        if selected_option in option_index_match:
            run_option = option_index_match[selected_option]

            # Quit when the user asks.
            if run_option == 'Quit':
                user_request_exit = True

            else:
                grab_analytics(run_option)

        else:
            # Get the users attention before going back to start of loop
            input("\n\n!! That is not a valid option, please try again. Press Enter to dismiss !!")


if __name__ == '__main__':
    sales_interaction_menu()