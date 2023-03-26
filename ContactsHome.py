# Name: Karina Kallas
# Class: CS361
# Last Edited: March 1, 2023
# File Name: Contacs Home
# Description: The Contacts Home message. Allows for welcome message, requests input number to move
#               to next screen, calls AddContacts, SeeContacts, DeleteContacts, and Messages. All
#               contacts pages use a microservice to provide data storage and access.


# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
import FileMergeProject.ContactsFiles.AddContacts
import FileMergeProject.ContactsFiles.SeeContacts
import FileMergeProject.ContactsFiles.DeleteContacts
import FileMergeProject.Messages.MessagesError


# --------------------------- #
# ---- HELPER FUNCTIONS  ---- #
# --------------------------- #
""" 
Helper functions to add, see all, or delete contacts.
Also includes an option with message to ask if client wants to 
return to Contacts Home.
"""


def add_contacts():
    # Add a contact using ContactMicro
    FileMergeProject.ContactsFiles.AddContacts.enter_contact()


def see_contacts():
    # See all contacts using ContactMicro
    FileMergeProject.ContactsFiles.SeeContacts.see_contacts()


def delete_contacts():
    # Delete a contact using ContactMicro
    FileMergeProject.ContactsFiles.DeleteContacts.delete_contacts()
    return


def back_to_home(num):
    # allows client to return back to contacts home
    if num == 2:
        home_choice()
    else:
        FileMergeProject.Messages.MessagesError.general_error()
        print("We are sending you back to contacts home.")
        home_choice()


# --------------------------- #
# ---------   MAIN  --------- #
# ------- CONTACTS HOME  ---- #
# --------------------------- #
def home_choice():
    print("\n"
          "\n...................."
          "\n....CONTACTS HOME..."
          "\nYou pressed 1 to add, manage, or search contents.\nWould you like to ...?"
          "\nPress 1: To add a new contact."
          "\nPress 2: To see all contacts. "
          "\nPress 3: To delete a Contact."
          "\nPress 4: To return to HOME.\n")
    choice = int(input())

    if choice == 1:
        add_contacts()
        home_choice()
    elif choice == 2:
        see_contacts()
        see_home = input("Press any number to return to contacts home: ")
        if see_home:
            home_choice()
    elif choice == 3:
        delete_contacts()
        see_home = input("Press any number to return to contacts home: ")
        if see_home:
            home_choice()
