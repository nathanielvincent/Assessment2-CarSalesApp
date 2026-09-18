# Nathaniel Vincent
# nav0135@arastudent.ac.nz
# A program to read car sale data from a .csv

from analytics_grabber import grab_analytics
from constants import *
from global_functions import *

import os

def _find_csv_files(directory: str) -> dict:
    """
    Finds all the .csv files in the given directory, including subdirectories.

    :param directory: The directory to scan for files
    :return: A dictionary where the keys are human readable, and the values are absolute paths.
    """

    csv_files = {}
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                # Build the full path to the file.
                full_path = os.path.join(folder, file)
                csv_files[file] = full_path # Use full path for the value, just the file name for the keys.

    return csv_files

def handle_file_picking() -> str:
    """
    Handles choosing which CSV file the code should use.
    Asks the user for their input if more than one are detected.

    :return:
    """

    csv_files = _find_csv_files('./')
    if len(csv_files) == 0:
        print("!! No CSV files in working directory !!")
        return ""

    else:
        valid_option = False

        # Shut up the python interpreter/type checker/whatever its called.
        selected_option = ""
        option_index_match = {}

        while not valid_option:
            clear_terminal()
            option_index_match = {}
            print("Detected multiple CSV files, which option would you like to pick?")
            for index, file in enumerate(csv_files, start=1):
                print(f"{index}. {file}")
                option_index_match[str(index)] = file

            selected_option = input("\nWhich option would you like to use? (Use the numbers!) ").lower().strip()
            if selected_option in option_index_match:
                valid_option = True

            else: # User is being difficult, scream at them.
                input("\n\n!! That is not a valid option, please try again. Press Enter to dismiss !!")

        selected_file = option_index_match[selected_option]
        selected_file_path = csv_files[selected_file]

    return selected_file_path

def sales_interaction_menu() -> None:
    """
    Runs a menu of data analysis options until the user requests a quit.

    :return: Nothing.
    """

    option_index_match = {}
    user_request_exit = False

    selected_file = handle_file_picking()
    clear_terminal()  # Clear the starting call line so it reads nicer.

    while not user_request_exit:
        print("Which option would you like to pick?")
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
                grab_analytics(run_option, selected_file)

        else:
            # Get the users attention before going back to start of loop
            input("\n\n!! That is not a valid option, please try again. Press Enter to dismiss !!")
            clear_terminal()


if __name__ == '__main__':
    sales_interaction_menu()