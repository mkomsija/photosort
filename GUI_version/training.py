# -----------------------------------------------------------
# Small app with GUI used for sorting all the files in a directory (including
# its subdirectories) by year and month of last modification. The inputs are
# the source and destination directories. The user is informed about the results
# in small notification windows.
#
# The interface is simple because the main focus was functionality and to practice
# python. 
#
# Variable naming convention:
# s - strings
# t - tuple
#   - complex type or class
#
# Created by:  Mihajlo Karlicic
# Created on:  14.01.2020 
# -----------------------------------------------------------


import tkinter as tk                                        # very simple GUI options
from photo_sort import *                                    # file sorting function

def create_done_window():
    done = tk.Tk()
    done.title("Done")
    done.geometry("200x100")
    done.resizable(0,0)

    # Done label
    done_label = tk.Label(done, text="Finished successfully!")
    done_label.place(relx = 0.5, rely = 0.25,anchor=tk.CENTER)

    # OK button
    ok_button = tk.Button(done, text="OK", width=10, height= 1, command=done.destroy)
    ok_button.place(relx=0.5, rely=0.7,anchor = tk.CENTER)
    
    done.mainloop()

def create_error_window(ERROR_FLAG):
    t_error_types = ("File path ", "Unknown ")

    error = tk.Tk()
    error.title("Error")
    error.geometry("220x100")
    error.resizable(0,0)

    # Error label
    s_error_title = t_error_types[ERROR_FLAG] + "error ocurred!"
    error_label = tk.Label(error, text=s_error_title)
    error_label.place(relx = 0.5, rely = 0.25,anchor=tk.CENTER)

    # OK button
    ok_button = tk.Button(error, text="OK", width=10, height= 1, command=error.destroy)
    ok_button.place(relx=0.5, rely=0.7,anchor = tk.CENTER)
    
    error.mainloop()

def get_paths(source_entry,dest_entry):
    # read Entry widgets and call sorting function  
    s_source_path = source_entry.get()
    s_dest_path = dest_entry.get()
    try:
        start_sorting(s_source_path,s_dest_path)
        master.destroy()
        create_done_window()
    except FileNotFoundError:
        master.destroy()
        create_error_window(0)
    except:
        master.destroy()
        create_error_window(1)


        
# Master window settings
master = tk.Tk()
master.title("Enter paths for sorting")
master.geometry("400x150")
master.resizable(0,0)

# First label
source_label = tk.Label(master, text="Source path:")
source_label.place(relx = 0.05, rely = 0.06,anchor=tk.NW)

# First entry
source_entry = tk.Entry(master, width = 59)
source_entry.place(relx = 0.05, rely = 0.19,anchor=tk.NW)

# Second label
dest_label = tk.Label(master, text="Destination path:")
dest_label.place(relx = 0.05, rely = 0.4,anchor=tk.NW)

# Second entry
dest_entry = tk.Entry(master, width = 59,)
dest_entry.place(relx = 0.05, rely = 0.53,anchor=tk.NW)

# OK button
# lambda in Button method is used as a workaround
# if command is not a lambda function and has arguments, it will run the command function at once, not at button press
ok_button = tk.Button(master, text="OK", width=10, height= 1, command=lambda:get_paths(source_entry,dest_entry))
ok_button.place(relx=0.52, rely=0.77,anchor = tk.NW)

# Cancel button
cancel_button = tk.Button(master, text="Cancel", width=10, height= 1, command=master.destroy)
cancel_button.place(relx=0.75, rely=0.77,anchor = tk.NW)

master.mainloop()
