from tkinter import *
from tkinter import messagebox
import sqlite3

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False,False)