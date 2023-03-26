# Name: Karina Kallas
# Class: CS361
# Last Edited: March 12, 2023
# File Name: File Merge Home UI
# Description: The UI for the main file merge message. Allows for selecting two files, copying files,
#               and merging to a new file.

# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
import pandas as pd


# --------------------------- #
# ---- Helper Functions ----- #
# --------------------------- #
def add_file_to_frame(data_frame, file_list):
    """
    Takes a list of .xlsx files to merge, reads the data, and copies data into data_frame.
    :param data_frame: an empty data_frame to save excel files
    :param file_list: list of all .xlsx files to merge
    :return: data_frame - a list of the data to be merged
    """
    for file in file_list:
        data_frame.append(pd.read_excel(file, header=0))

    return data_frame


def get_new_name():
    """
    Asks for a new name for the merged file.
    :return: new_name - a string representing the new name for the .xlsx file
    """
    print("Please enter a name for your new file."
          "\n   Ex. mergedfile.xlsx")
    new_name = input("New file name: ")
    return new_name


# --------------------------- #
# ------------  MAIN -------- #
# --------  Merge Files ----- #
# --------------------------- #
def merge_files(file_list):
    """
    Takes a list of .xlsx files and merges them into a new document that takes the name
    given by the user.
    :param file_list: A list of files to merge
    :return: None (But does save a new .xlsx file to local.)
    """
    data_frame = []

    # save files in list
    add_file_to_frame(data_frame, file_list)
    for file in data_frame:
        file['Date'] = file['Date'].astype(str)

    # concat dataframes and format date
    new_file = pd.concat(data_frame, axis=0, ignore_index=True)
    new_file.columns = new_file.columns.str.title()

    # get user name and check that has .xlsx
    new_name = get_new_name()
    if len(new_name) < 5 or new_name[-5:] != '.xlsx':
        print("\nOops! You forgot to use '.xlsx' in your file name.")
        new_name = new_name+".xlsx"
        print(f"We have added the correct extension: {new_name} \n")

    # export as xlsx with user selected name
    print(f"\n...saving file << {new_name} >> to FileMergeProject folder...")
    new_file.to_excel(new_name, index=False)
    print("\nYour new file has been created in the 'FileMergeProject' folder under the name:"
          f"{new_name}.")
