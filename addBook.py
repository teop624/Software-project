from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('Libarary.db')
cur = con.cursor()

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

        #name
        self.lbl_name = Label(self.bottomFrame, text = 'Book Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_name.place(x = 40, y = 40)
        self.ent_name = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_name.insert(0, 'Enter Book Name')
        self.ent_name.place(x = 150, y = 45)
        #author
        self.lbl_author = Label(self.bottomFrame, text = 'Author', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_author.place(x = 40, y = 80)
        self.ent_author = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_author.insert(0, 'Enter Author Name')
        self.ent_author.place(x = 150, y = 85)
        #page
        self.lbl_page = Label(self.bottomFrame, text = 'No. of Pages', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_page.place(x = 40, y = 120)
        self.ent_page = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_page.insert(0, 'Enter No. of Pages')
        self.ent_page.place(x = 150, y = 125)
        #year
        self.lbl_year = Label(self.bottomFrame, text = 'Year', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_year.place(x = 40, y = 160)
        self.ent_year = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_year.insert(0, 'Enter Year')
        self.ent_year.place(x = 150, y = 165)
        #button
        button = Button(self.bottomFrame, text = 'Add Book', command = self.addBook)
        button.place(x = 270, y = 200)

    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        year = self.ent_year.get()

        if name and author and page and year !='':
            try:
                query = "INSERT INTO 'books' (bookName, bookAuthor, pageCount, year) VALUES(?,?,?,?)"
                cur.execute(query, (name, author, page, year))
                con.commit()
                messagebox.showinfo('Success', 'Book added successfully', icon = 'info')

            except:
                messagebox.showerror('Error', 'Cannot add data to Database', icon = 'error')
        
        else:
            messagebox.showerror('Error', 'Please fill all the fields', icon = 'warning')
                
