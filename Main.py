# Name: Karina Kallas
# Class: CS361
# Last Edited: Jan 26, 2022
# File Name: Home UI
# Description: The UI for the main message. Allows for welcome message, requests input number to move
#               to next screen, and allows for exit.

import ContactsHome

count = 1

def request_input():
    input_num = 0
    while input_num <1 or input_num >3:
        print("...HOME...")
        print("Please select an option:\n...\nPress 1: To add, manage, or search contacts.\nPress 2: To merge data files.\nPress 3: To exit.")
        input_num = int(input())
        if input_num <1 or input_num >3:
            print("\n******\nInvalid option. Please try again.\n******\n")
    return input_num


def welcome_message():
    print("\nWelcome to File Merger HOME\n")
    print("***Adding contacts saves time when sharing documents!***\n")


while True and count < 3:
    #say hello only the first time
    if count == 1:
        count += 1
        welcome_message()
    
    # Get an input number.
    input_num = request_input()

    # selected 1 and wants to edit emails
    if input_num == 1:
        ContactsHome.home_choice()
        
    # selected 2 and wants to merge files
    elif input_num == 2:
        print("Under construction...")

    # Exit program
    elif input_num == 3:
        exit("You entered 3 to exit. Good bye.")