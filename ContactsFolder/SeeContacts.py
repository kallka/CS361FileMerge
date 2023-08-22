# Name: Karina Kallas
# Class: CS361
# Last Edited: March 9, 2023
# File Name: Home UI
# Description: See all contacts using microservice ContactsMicro.

# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
from bs4 import BeautifulSoup
import requests


# --------------------------- #
# ----- MAIN FUNCTION ------- #
# ------ see_contacts ------- #
# --------------------------- #
def see_contacts():
    """
    1.) Get the home page html text using request.get - home page contains a table with all contacts.
    2.) Use BeautifulSoup and lxml to save into readable file "soup"
    3.) Save the data from the rows in a variable and loop to print all data. (data = contact info)
    """
    # Alert "gettting contacts"
    print("...getting contacts...")

    # Get the html text in readable soup file from home page.
    counter = 0
    html_text = requests.get('http://127.0.0.1:5000/').text
    soup = BeautifulSoup(html_text, 'lxml')

    # Save Row Tags:
    row_tags = soup.find_all('td')

    # Print the data in the Row Tags.
    # Skip first 3 items as this will correspond to column headers
    #   as column headers were also identified using 'td'
    print(" [ CURRENT CONTACTS ] ")
    print("\n [ -- START -- ] ")
    for row in row_tags:
        if counter % 3 == 0 and counter != 0:
            print(".\n")
        if counter > 2:
            print(row.text)
        counter += 1

    print(" [ -- END CONTACTS -- ] ")
