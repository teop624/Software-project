from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
import sqlite3
con = sqlite3.connect('Libarary.db')
cur = con.cursor()

class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x400+600+250")
        self.title("Give Book")
        self.resizable(False,False)
        self.topFrame = Frame(self, height = 150, bg = 'white')
        self.topFrame.pack(fill = X)
        self.bottomFrame = Frame(self, height = 600, bg = '#fcc324')
        self.bottomFrame.pack(fill = X)
        global given_id
        self.book_id = int(given_id)

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

        #heading, image & date
        self.top_image = PhotoImage(file = 'icons/givebook.png')
        top_image_lbl = Label(self.topFrame, image = self.top_image, bg = 'white')
        top_image_lbl.place(x = 120, y = 10)
        heading = Label(self.topFrame, text = 'Give Book', font = 'arial 22 bold', bg = 'white', fg = '#003f8a')
        heading.place(x = 200, y = 60)

        #book name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text = 'Book Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_name.place(x = 40, y = 40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable = self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.current(self.book_id - 1)
        self.combo_name.place(x = 150, y = 45)
        #member name
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottomFrame, text = 'Member Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_member.place(x = 40, y = 80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable = self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x = 150, y = 85)
        #button
        button = Button(self.bottomFrame, text = 'Give Book', command = self.giveBook)
        button.place(x = 150, y = 120)
    def giveBook(self):
        book_name = self.book_name.get()
        self.book_id = book_name.split('-')[0]
        member_name = self.member_name.get()

        if(book_name and member_name !=''):
            try:
                query = "INSERT INTO 'borrows' (bbook_id, bmember_id) VALUES(?,?)"
                cur.execute(query,(book_name, member_name))
                con.commit()
                messagebox.showinfo('Success', 'Book Borrowed Successfully', icon = 'info')
                cur.execute("UPDATE books SET status =? WHERE bookID =?", (1, self.book_id))
                con.commit()
                self.destroy()
            except:
                messagebox.showerror('Error', 'Something went wrong', icon = 'error')

        else:messagebox.showerror("Error", "Please fill all the details", icon = 'warning')