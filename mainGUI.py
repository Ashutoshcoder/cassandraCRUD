"""
Author : Ashutosh Kumar
Version : 1.1
Description : GUI for the Cassandra File
Email : ashutoshkumardbms@gmail.com
"""

# using Tkinter module for GUI
import tkinter
from deletePatientData import *
from insertPatientData import *
from selectPatientData import *

# intializing the window with the given object
window = tkinter.Tk()
window.title("Cassandra CRUD Operation")  # to rename the title of the window
window.geometry("312x324")  # Minimum size of the geometry window
window.resizable(0, 0)  # To prevent resizing of the window


# Different functions to be called for different operations
def insert_data_cassandra():
    insertBulkData()
    tkinter.Label(window, text="Data Inserted!").pack()

def delete_data_cassandra():
    deleteAllData()
    tkinter.Label(window, text="All Data Inserted!").pack()

def delete_single_data_cassandra():
    deleteSingleData()
    tkinter.Label(window, text="Data Deleted For Single Entry!").pack()

def select_data_cassandra():
    selectAllData()
    tkinter.Label(window, text="Selected Data For Single Entry!").pack()


tkinter.Button(window, text="Insert Data!", command=insert_data_cassandra).pack()
tkinter.Button(window, text="Update Data!", command=insert_data_cassandra).pack()
tkinter.Button(window, text="Delete Data!", command=delete_data_cassandra).pack()
tkinter.Button(window, text="Delete Single Data Entry!", command=delete_single_data_cassandra).pack()
tkinter.Button(window, text="Select All Data!", command=select_data_cassandra).pack()

window.mainloop()
