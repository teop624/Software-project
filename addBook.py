from tkinter import *
from tkinter import messagebox
import sqlite3

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False,False)

        #top frame
        self.topFrame = Frame(self, height = 150, bg = 'white')
        self.topFrame.pack(fill = X)
        #bottom frame
        self.bottomFrame = Frame(self, height = 600, bg = '#fcc324')
        self.bottomFrame.pack(fill = X)
        #heading, image & date
        self.top_image = PhotoImage(file = 'icons/addbook.png')
        top_image_lbl = Label(self.topFrame, image = self.top_image, bg = 'white')
        top_image_lbl.place(x = 120, y = 10)
        heading = Label(self.topFrame, text = 'Add Book', font = 'arial 22 bold', bg = 'white', fg = '#003f8a')
        heading.place(x = 290, y = 60)