# Name: Karina Kallas
# Class: CS361
# Last Edited: March 9, 2023
# File Name: Home UI
# Description: Delete a contact using microservice ContactsMicro.

# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
from playwright.sync_api import sync_playwright
from FileMergeProject.ContactsFiles.SeeContacts import see_contacts


# --------------------------- #
# ----- MAIN FUNCTION ------- #
# ----- delete_contacts ----- #
# --------------------------- #
def delete_contacts():
    """
    1.) Asks client if they would like to see all contacts. (As contact needs to be deleted by name.)
    2.) Request name of contact to be deleted.
    2.) Use playwright to open the page needed, fill in input field, and click button to submit changes.
    """
    # Ask if need to see contact names and then try to delete by name.
    print("Please delete a contact by their name.")
    yes_no = input("Would you like to see all your contacts first? \n - Enter 1 for yes. \n - Enter 2 for no.\n >")
    yes_no = int(yes_no)
    if yes_no == 1:
        "Your Contacts: \n"
        see_contacts()
    print("\n")
    name = input("Please enter the name of the contact you wish to delete: ")
    print(name)

    # connect to microservice and send information
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:5000/remove_contacts')
        page.fill('input#name', name)
        page.click('input[type=submit]')

    print("...deleting contact...")
    print(f"Contact {name} was deleted.")
