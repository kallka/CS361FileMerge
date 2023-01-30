# Description: Find all contacts, search for some contacts, 

import ContactsHome

def delete_contact():
    print("... under construction ...")
    return

def search_contact():
    print("... under construction ...")
    return

def print_all():
    print("\nYou pressed 1 to view all contacts. Please see below ...")
    file = open("contacts.txt", "r")
    lines = file.readlines()
    print("Complete Contact List")
    counter = 1
    for line in lines:
        if counter == 1:
            print("ID:", counter)
        if "[STOP]" in line:
            counter += 1
            print("ID:", counter)
        else:
            print("      "+line)

    print("Would you like to:")
    print("Press 1: To Delete a Contact by ID.\n Press 2: To find new contacts. \n Press 3: To return to CONTACTS HOME.")
    choice = input()
    if int(choice) == 1:
        delete_contact()
        return
    if int(choice) == 2:
        find_contact()
        return
    if int(choice) == 3:
        ContactsHome.home_choice()
        return

def find_contact():
    print("You pressed 2 find, edit or delete a contact.")
    print("Would you like to:")
    print("Press 1: To view all contacts. \nPress 2: To search for a contact. \n Press 3: To delete a contact.")
    print("Press 4: To return to CONTACTS HOME. \n Press 5: To return to HOME.")
    choice_1 = input()

    if int(choice_1) == 1:
        print_all()
    if int(choice_1) == 2:
        search_contact()
    if int(choice_1) == 3:
        delete_contact()
    if int(choice_1) == 4:
        ContactsHome.home_choice()
    else:
        return

