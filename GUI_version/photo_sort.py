# -----------------------------------------------------------
# Script used to iterate trough a folder and all its subfolders in order to sort
# all the individual files by month and year of last modification. Input and output
# folders must both exist and have valid paths.
#
# Variable naming convention:
# s - strings
#   - complex type or class
#
# Created by:  Mihajlo Karlicic
# Created on:  10.01.2020
# Modified on: 14.01.2020
# -----------------------------------------------------------

import os                                               # for file manipulation
from datetime import datetime                           # for date format conversion
import shutil                                           # for copying files

s_dest_path = ""
# month folder names list - currently in Serbian
MONTHS = ["01 - Januar",
          "02 - Februar",
          "03 - Mart",
          "04 - April",
          "05 - Maj",
          "06 - Jun",
          "07 - Jul",
          "08 - Avgust",
          "09 - Septembar",
          "10 - Oktobar",
          "11 - Novembar",
          "12 - Decembar"]


# file sorting function
def sort_file(entry):
    # get a file's info and put it in the right folder
    # if the right folder doesn't exist create it
    
    fileInfo = entry.stat()                                                      
    date = datetime.fromtimestamp(fileInfo.st_mtime).strftime('%m %Y')  # convert to mY format
    s_file_dest_year = s_dest_path + "/" + date[3:] 
    if not os.path.exists(s_file_dest_year):                            # check whether year folder exists
        os.mkdir(s_file_dest_year)
    s_file_dest_month = s_file_dest_year + "/" + MONTHS[int(date[0:2]) - 1]
    if not os.path.exists(s_file_dest_month):                           # check whether month folder exists
        os.mkdir(s_file_dest_month)
    shutil.copy2(entry.path, s_file_dest_month)                         # copy file
    
# recursing function for iterating all subfolders
def enter_subfolder(entry):
    # enter a subfolder and sort its files
    # if there are more subfolders sort their files too

    with os.scandir(entry) as sub_entries:
        for sub_entry in sub_entries:
            if sub_entry.is_dir():
                enter_subfolder(sub_entry)                              # recurse
            elif sub_entry.is_file():
                sort_file(sub_entry)                                
            else:
                pass
    

# safely open folder and process it
def start_sorting(s_source_path, s_dest_path_ext):
    global s_dest_path
    s_dest_path = s_dest_path_ext
    with os.scandir(s_source_path) as start_folder:
        for entry in start_folder:
            if entry.is_dir():
                 enter_subfolder(entry)
            elif entry.is_file():
                 sort_file(entry)
            else:
                 pass                    # we should never get here

