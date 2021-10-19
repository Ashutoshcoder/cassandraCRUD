"""
Author : Ashutosh Kumar
Version : 1.0
Description : Main GUI For Python Application
Email : ashutoshkumardbms@gmail.com
"""

import tkinter as tk
import tkinter.font as tkFont
from deletePatientData import *
from insertPatientData import *
from selectPatientData import *
from updatePatientData import *

class App:
    def __init__(self, root):
        # setting title
        root.title("Cassandra GUI")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        insertButton = tk.Button(root)
        insertButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        insertButton["font"] = ft
        insertButton["fg"] = "#000000"
        insertButton["justify"] = "center"
        insertButton["text"] = "Insert Data "
        insertButton.place(x=40, y=110, width=113, height=41)
        insertButton["command"] = self.insertButton_command

        headerForGUI = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        headerForGUI["font"] = ft
        headerForGUI["fg"] = "#333333"
        headerForGUI["justify"] = "center"
        headerForGUI["text"] = "Cassandra GUI"
        headerForGUI.place(x=160, y=40, width=236, height=30)

        deleteButton = tk.Button(root)
        deleteButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        deleteButton["font"] = ft
        deleteButton["fg"] = "#000000"
        deleteButton["justify"] = "center"
        deleteButton["text"] = "Delete Data"
        deleteButton.place(x=40, y=170, width=114, height=40)
        deleteButton["command"] = self.deleteButton_command

        selectButton = tk.Button(root)
        selectButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        selectButton["font"] = ft
        selectButton["fg"] = "#000000"
        selectButton["justify"] = "center"
        selectButton["text"] = "Select Data "
        selectButton.place(x=40, y=230, width=115, height=40)
        selectButton["command"] = self.selectButton_command

        selectButton = tk.Button(root)
        selectButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        selectButton["font"] = ft
        selectButton["fg"] = "#000000"
        selectButton["justify"] = "center"
        selectButton["text"] = "Select Data "
        selectButton.place(x=40, y=230, width=115, height=40)
        selectButton["command"] = self.selectButton_command

        updateMessageUpdate = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        updateMessageUpdate["font"] = ft
        updateMessageUpdate["fg"] = "#333333"
        updateMessageUpdate["justify"] = "center"
        updateMessageUpdate["text"] = "Update Message"
        updateMessageUpdate.place(x=180, y=290, width=272, height=30)

        updateButton = tk.Button(root)
        updateButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        updateButton["font"] = ft
        updateButton["fg"] = "#000000"
        updateButton["justify"] = "center"
        updateButton["text"] = "Update Data"
        updateButton.place(x=40, y=290, width=112, height=42)
        updateButton["command"] = self.updateButton_command()

        insertMessageUpdate = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        insertMessageUpdate["font"] = ft
        insertMessageUpdate["fg"] = "#333333"
        insertMessageUpdate["justify"] = "center"
        insertMessageUpdate["text"] = "Insert Message"
        insertMessageUpdate.place(x=190, y=120, width=255, height=30)

        deleteMessageUpdate = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        deleteMessageUpdate["font"] = ft
        deleteMessageUpdate["fg"] = "#333333"
        deleteMessageUpdate["justify"] = "center"
        deleteMessageUpdate["text"] = "Delete Message"
        deleteMessageUpdate.place(x=200, y=180, width=235, height=30)

        selectMessageUpdate = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        selectMessageUpdate["font"] = ft
        selectMessageUpdate["fg"] = "#333333"
        selectMessageUpdate["justify"] = "center"
        selectMessageUpdate["text"] = "Select Message"
        selectMessageUpdate.place(x=190, y=230, width=251, height=30)

        closeButton = tk.Button(root)
        closeButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        closeButton["font"] = ft
        closeButton["fg"] = "#000000"
        closeButton["justify"] = "center"
        closeButton["text"] = "Close App"
        closeButton.place(x=260, y=410, width=108, height=39)
        closeButton["command"] = self.closeButton_command

    def insertButton_command(self):
        insertBulkData()
        print("Data Insert Completed")

    def deleteButton_command(self):
        deleteAllData()
        print("All Data Deleted")

    def deleteSingleRecordButton(self):
        deleteSingleData()
        print("Single Record Deleted")

    def selectButton_command(self):
        selectAllData()
        print("Data Selected")

    def closeButton_command(self):
        print("Close App")

    def updateButton_command(self):
        updateSingleData()
        return True;

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
