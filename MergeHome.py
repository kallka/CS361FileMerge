# Name: Karina Kallas
# Class: CS361
# Last Edited: March 12, 2023
# File Name: File Merge Home UI
# Description: The UI for the main file merge message. Allows for selecting two files, copying files,
#               and merging to a new file.

# --------------------------- #
# --------- IMPORTS  -------- #
# --------------------------- #
import FileMergeProject.FileMergeFiles.GetFiles


# --------------------------- #
# ---------- MAIN  ---------- #
# ------- FILE MERGE -------- #
# -------- HOME PAGE -------- #
# --------------------------- #
def home_choice():
    print("\n"
          "\n...................."
          "\n.....MERGE HOME....."
          "\nYou pressed 2 to merge data files. \nWould you like to ...?"
          "\nPress 1: To select and merge files."
          "\nPress 3: To return to HOME.\n")
    choice = input("> ")

    if int(choice) == 3:
        return
    else:
        FileMergeProject.FileMergeFiles.GetFiles.get_file_info()
        print("\n\n")
