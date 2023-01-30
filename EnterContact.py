import  MessagesSuccess
import  MessagesError
import  ContactsHome


def contact_to_file(new_contact):
    contact_file = open("contacts.txt", "a")
    contact_string = ""
    for item in new_contact:
        contact_string += item + "\n"
    contact_string += "[STOP]\n"
    contact_file.write(contact_string)
    contact_file.close()
    return

def enter_contact():
    fname = input("First Name:")
    lname = input("Last Name:")
    title = input("Title:")
    organization = input("Organization:")
    project = input("Project:")
    email = input("Email:")
    phone = input("Phone:")
    new_contact = [fname, lname, title, organization, project, email, phone]

    #check if correct
    print("\nYou entered the following contact...")
    print("First Name:", fname)
    print("Last Name:", lname)
    print("Title:", title)
    print("Organization:", organization)
    print("Project:", project)
    print("Email:", email)
    print("phone", phone)
    print("Is the above entry correct?")
    confirm = input("Y/N: ")

    if confirm == "N":
        print("Would you like to try again or go back to HOME?")
        print("Press 1: To try again. \nPress 2: To go back to CONTACTS HOME. \nPress 3: To go back to HOME.")
        choice_2 = input()
        if int(choice_2) == 1:
            print(MessagesError.try_again())
            enter_contact()
        if int(choice_2) == 2:
            ContactsHome.home_choice()
        else:
            return
    else:
        contact_to_file(new_contact)
        print(MessagesSuccess.input_entered())
        print("Would you like to try again or go back to HOME?")
        print("Press 1: To enter a new contact. \nPress 2: To go back to CONTACTS HOME. \n Press 3: To go back HOME.")
        choice_2 = input()
        if int(choice_2) == 1:
            enter_contact()
        if int(choice_2) == 2:
            ContactsHome.home_choice()
        else:
            return