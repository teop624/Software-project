from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
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
        self.topFrame = Frame(self, height = 150, bg = 'white')
        self.topFrame.pack(fill = X)
        self.bottomFrame = Frame(self, height = 600, bg = '#fcc324')
        self.bottomFrame.pack(fill = X)

        #self.book_id = int(book_id)

        #heading
        self.top_image = PhotoImage(file = 'icons/returnbook.png')
        top_image_lbl = Label(self.topFrame, image = self.top_image, bg = 'white')
        top_image_lbl.place(x = 120, y = 10)
        heading = Label(self.topFrame, text = 'Return Book', font = 'arial 22 bold', bg = 'white', fg = '#003f8a')
        heading.place(x = 290, y = 60)
        
        query = "SELECT bookID, bookName FROM books WHERE status = 1"
        borrowed_books = cur.execute(query).fetchall()

        book_list = []
        for book in borrowed_books:
            book_list.append(str(book[0]) + '-' + book[1])

        #book name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text = 'Book Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_name.place(x = 40, y = 40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable = self.book_name, state = "readonly")
        self.combo_name['values'] = book_list
        self.combo_name.place(x = 150, y = 45)
        self.combo_name.bind("<<ComboboxSelected>>", self.memberDropdown)
       
       #button
        button = Button(self.topFrame, text = 'Return Book', command = self.returnBook)
        button.place(x = 150, y= 120)

        #member name
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottomFrame, text = 'Member Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_member.place(x = 40, y = 80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable = self.member_name, state = "readonly")
        self.combo_member.place(x = 150, y = 85)

    def memberDropdown(self, evt):
        book_id = self.book_name.get().split('-')[0]
        query = "SELECT members.memberID, members.memberName FROM members INNER JOIN borrows ON members.memberID = borrows.memberID WHERE borrows.bookID = ?"
        members = cur.execute(query, (book_id,)).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + '-' + member[1])
        self.combo_member['values'] = member_list
        if member_list:
            self.combo_member.current(0)
        else:
            self.combo_member.set('')
        
    def returnBook(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()
        book_id = int(book_name.split('-')[0])
        return_date = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')

        if not book_name or not member_name:
            messagebox.showerror("Error", "Please select a book and member.", icon='warning')
            return

        try:
            cur.execute("UPDATE books SET status = ? WHERE bookID = ?", (0, book_id,))
            con.commit()
            cur.execute("UPDATE borrows SET returnDate = ? WHERE bookID = ?", (return_date, book_id,))
            con.commit()
            messagebox.showinfo("Success", "Book Returned Successfully", icon = 'info')
            self.destroy()

        except:
            messagebox.showerror("Error", "Something went wrong", icon = 'error')

  # def returnBook(self):
   #   try:
    #      cur.execute("UPDATE books SET status = ? WHERE bookID = ?", (0, self.book_id,))
     #     con.commit()
      #    cur.execute("DELETE FROM borrows WHERE bookID =?", (self.book_id,))
       #   con.commit()
        #  messagebox.showinfo("Success", "Book Returned Successfully", icon = 'info')
         # self.destroy()
      #except:
       #   messagebox.showerror("Error", "Something went wrong", icon = 'error')