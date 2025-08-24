from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
import datetime
import sqlite3
con = sqlite3.connect('Libarary.db')
cur = con.cursor()

class GiveBook(Toplevel):
    def __init__(self, book_id):
        Toplevel.__init__(self)
        self.geometry("400x400+600+250")
        self.title("Give Book")
        self.resizable(False,False)
        self.topFrame = Frame(self, height = 150, bg = 'white')
        self.topFrame.pack(fill = X)
        self.bottomFrame = Frame(self, height = 600, bg = '#fcc324')
        self.bottomFrame.pack(fill = X)

        self.book_id = int(book_id)

        query = "SELECT * FROM books WHERE status = 0"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + '-' + book[1])

        query2 = "SELECT * FROM members"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + '-' + member[1])


        #book name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text = 'Book Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_name.place(x = 40, y = 40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable = self.book_name, state = "readonly")
        self.combo_name['values'] = book_list
        self.combo_name.current(self.book_id - 1)
        self.combo_name.place(x = 150, y = 45)
        #member name
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottomFrame, text = 'Member Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_member.place(x = 40, y = 80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable = self.member_name, state = "readonly")
        self.combo_member['values'] = member_list
        self.combo_member.place(x = 150, y = 85)
        #date
        self.date = StringVar()
        self.lbl_date = Label(self.bottomFrame, text = 'Date Borrowed', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_date.place(x = 40, y = 120)
        self.combo_date = ttk.Combobox(self.bottomFrame, textvariable = self.date)
        self.combo_date['values'] = member_list
        self.combo_date.place(x = 150, y = 125)
        #button
        button = Button(self.bottomFrame, text = 'Give Book', command = self.giveBook)
        button.place(x = 150, y = 160)
                #heading, image & date
        self.top_image = PhotoImage(file = 'icons/givebook.png')
        top_image_lbl = Label(self.topFrame, image = self.top_image, bg = 'white')
        top_image_lbl.place(x = 120, y = 10)
        heading = Label(self.topFrame, text = 'Give Book', font = 'arial 22 bold', bg = 'white', fg = '#003f8a')
        heading.place(x = 200, y = 60)

    def giveBook(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()
   
        if (book_name and member_name !=''):
            book_id = book_name.split('-')[0]
            member_id = member_name.split('-')[0]
            cur.execute("SELECT status FROM books WHERE bookID = ?", (book_id,))
            book_status = cur.fetchone()[0]
            if book_status == 1:
                messagebox.showerror("Error", "Book is already issued", icon = 'warning')
                return
            date = datetime.date.today().strftime('%Y-%m-%d')
            query = "INSERT INTO 'borrows' (bookID, memberID, borrowDate) VALUES(?,?,?)"
            cur.execute("UPDATE books SET status =? WHERE bookID =?", (1, self.book_id))
            con.commit()
            messagebox.showinfo('Success', 'Book Borrowed Successfully', icon = 'info')
            self.destroy()
            

        else:
            messagebox.showerror("Error", "Please fill all the details", icon = 'warning')