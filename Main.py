# Name: Karina Kallas
# Class: CS361
# Last Edited: March 13, 2023
# File Name: Home UI
# Description: The UI for the main message. Allows for welcome message, requests input number to move
#               to next screen, and allows for exit.


# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
import FileMergeProject.ContactsHome
import FileMergeProject.MergeHome


# --------------------------- #
# --- GLOBAL CONSTANTS  ----- #
# --------------------------- #
count = 1


# --------------------------- #
# ---  Helper Functions  ---- #
# --------------------------- #
def request_input():
    """
    :description: Requests input - would the user like to go to "contacts" (add, manage, search), "file merge"
    (merge data files), or exit program.
    :return: input_num (represents the user's choice)
    """
    input_num = 0
    while input_num < 1 or input_num > 3:
        print("\n............"
              "\n....HOME...."
              "\n............")
        print(
            '''
            Please select an option:
            ...
            Press 1: To add, manage, or search contacts.
            Press 2: To merge data files.
            Press 3: To exit.
            ''')
        input_num = int(input("> "))
        if input_num < 1 or input_num > 3:
            print("\n******\nInvalid option. Please try again.\n******\n")
    return input_num


def welcome_message():
    """
    Prints a welcome message to screen.
    """
    print("\nWelcome to File Merger HOME"
          "\n***Adding contacts saves time when sharing documents!***\n")


# --------------------------- #
# ---------   MAIN  --------- #
# ------- HOME PAGE --------- #
# --------------------------- #
"""
Home page is a continuous while loop.
Welcome message only printed first time client visits page.
Requests input and directs to other pages.
"""


while True and count < 3:
    # say hello only the first time
    if count == 1:
        count += 1
        welcome_message()
    
    # Get an input number.
    input_num = request_input()

    # selected 1 and wants to edit emails
    if input_num == 1:
        FileMergeProject.ContactsHome.home_choice()
        
    # selected 2 and wants to merge files1
    elif input_num == 2:
        FileMergeProject.MergeHome.home_choice()

    # Exit program
    elif input_num == 3:
        exit("You entered 3 to exit. Good bye.")
