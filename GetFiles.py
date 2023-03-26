# Name: Karina Kallas
# Class: CS361
# Last Edited: March 13, 2023
# File Name: File Merge Home UI
# Description: The UI for the main file merge message. Allows for selecting two files, copying files,
#               and merging to a new file.

# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
from FileMergeProject.Messages import MessagesError
import FileMergeProject.FileMergeFiles.MergeFiles


# --------------------------- #
# ---  Helper Functions  ---- #
# --------------------------- #
def help_with_filepath():
    """
    Prints directions to help user select a file path.
    """
    system = input("Please enter 1 if you are a MAC user. Please enter 2 for PC.\n> ")
    if int(system) == 1:
        print("1.) Find the file you would like to select. "
              "\n2.) Control+click on the file and select 'Get Info'."
              "\n4.) Copy the text following 'Where:'. (ex. iCloud Drive > Desktop)"
              "\n5.) Paste this path directly into the terminal line followed by the file name.\n")
    else:
        print("1.) Open File Explorer and find the file you would like to select."
              "\n2.) Right click on your file and select 'Properties'."
              "\n3.) Under the 'General' tab copy the path following 'Location'."
              "\n4.) Paste this path directly into the terminal line followed by the file name.\n")


def confirm(select_list):
    """
    Confirms any selections by reading items from a list and asking for yes or no selection.
    :return: True if user confirmed selections. False otherwise.
    """
    print("\n ...Please confirm your selections...\n")
    length = len(select_list)
    for num in range(0, length):
        print(f"Is this ({num+1} of {length}) selection correct?")
        print("     - ", select_list[num])
        correct = input("(Y/N): ")
        if correct == "N":
            return False

    return True


def try_again():
    """
    Asks user if they would like to try merging files again.
    :return: True if want to try again. False if return home.
    """
    print("\n................"
          "\nWould you like to return home or try again?"
          "\nPress 1: To try again."
          "\nPress 2: To return to HOME.")
    choice = input("> ")

    if int(choice) == 1:
        return True
    else:
        return False


# --------------------------- #
# --------  MAIN  ----------- #
# -----  Get File Info  ----- #
# --------------------------- #
def get_file_info():
    """
    Requests file paths for two .xlsx files to merge. Sends to help_with_filepath function
    if user needs help with file path naming. Confirms the file path choices and sends
    file paths to MergeFiles.py to merge the .xlsx files.
    :return: None
    """
    # ask if user needs help merging files
    print("\n................")
    choice_1 = input("\nTo select files to merge, you need to enter a file path. "
                     "\n    ***Entering a file path saves memory space and time with large files.\n"
                     "\nDo you need help entering a file path? (Y/N): ")
    if choice_1 == "Y":
        help_with_filepath()

    # get file path
    print("Great! We are ready to go! \n"
          "     Please enter the file paths for your two .xlsx files, below ...."
          "\n         - Example: Users/documents/file1.xlsx")
    merge_file1 = input("Enter location of 1st file to merge:")
    merge_file2 = input("Enter location of 2nd file to merge:")
    file_list = [merge_file1, merge_file2]

    # confirm selections - confirm takes a list as parameter
    accept = confirm(file_list)

    # merge files or try again
    if accept is True:
        FileMergeProject.FileMergeFiles.MergeFiles.merge_files(file_list)
    else:
        print(MessagesError.general_error())

    # ask if client would like to merge more files or return to home screen
    choice = try_again()

    if choice is True:
        get_file_info()
    else:
        return
