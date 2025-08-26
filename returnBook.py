from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
import sqlite3
import datetime

con = sqlite3.connect('Libarary.db')
cur = con.cursor()

class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Return Book")
        self.resizable(False,False)

        #frame
        self.Frame = Frame(self, height = 750, width = 650)
        self.frame.pack()
        self.book_id = int(book_id)
        
        #book info
        book_info = cur.execute("SELECT * FROM books WHERE bookID = ?", (self.book_id,)).fetchone()
        borrow_info = cur.execute("SELECT * FROM borrows WHERE bookID = ?", (self.book_id,)).fetchone()
        member_info = cur.execute("SELECT * FROM members WHERE memberID = ?", (borrow_info[2],)).fetchone()
        