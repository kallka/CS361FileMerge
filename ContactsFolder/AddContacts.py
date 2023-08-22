# Name: Karina Kallas
# Class: CS361
# Last Edited: March 9, 2023
# File Name: Home UI
# Description: Add a contact using microservice ContactsMicro.

# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
from playwright.sync_api import sync_playwright
import time


# --------------------------- #
# ----- MAIN FUNCTION ------- #
# ----- enter_contact ------- #
# --------------------------- #
def enter_contact():
    """
    1.) Requests info for new contact: name, email, phone.
    2.) Use playwright to open the page needed, fill input fields, and click button to submit changes.
    """

    # gather information from client: name/email/phone
    print("Please enter your new contact ...")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    # connect to microservice and send information
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:5000/enter_new')
        page.fill('input#name', name)
        page.fill('input#email', email)
        page.fill('input#phone', phone)
        time.sleep(3)
        page.click('input[type=submit]')

    print("...submitting contact...")
    print("Contact Submitted!")
