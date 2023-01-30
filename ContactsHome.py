# Name: Karina Kallas
# Class: CS361
# Last Edited: Jan 26, 2022
# File Name: Contacs Home
# Description: The Contacts Home message. Allows for welcome message, requests input number to move
#               to next screen, and allows for exit.

import MessagesError
import MessagesSuccess
import ContactsFiles.ContactsSearch
import ContactsFiles.EnterContact
import ContactsFiles.FindContact

count = 0

def home_choice():
    print("\n....CONTACTS HOME...")
    print("You pressed 1 to add, manage, or search contents.\nWould you like to ...?")
    print("Press 1: To add a new contact.\nPress 2: To find, edit or delete a contact. \nPress 3: To return to HOME.\n")
    choice = input()
    choice = int(choice)

    if choice == 1:
        ContactsFiles.EnterContact.enter_contact()
    elif choice == 2:
        ContactsFiles.FindContact.find_contact()
    else:
        return 1

#while True:
#    if count == :
#        count += 1
#        print("ContactsHome.py is running")
    
    # check if we need to run home
#    file_read = open("call-next.txt", "r")
#    lines = file_read.readlines()
#    file_read.close()
    
#    if "contacts home" in lines:
#        contacts_main()


