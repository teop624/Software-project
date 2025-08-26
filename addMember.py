from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('Libarary.db')
cur = con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Member")
        self.resizable(False,False)

        #top frame
        self.topFrame = Frame(self, height = 150, bg = 'white')
        self.topFrame.pack(fill = X)
        #bottom frame
        self.bottomFrame = Frame(self, height = 600, bg = '#fcc324')
        self.bottomFrame.pack(fill = X)
        #heading, image & date
        self.top_image = PhotoImage(file = 'icons/addmember.png')
        top_image_lbl = Label(self.topFrame, image = self.top_image, bg = 'white')
        top_image_lbl.place(x = 120, y = 10)
        heading = Label(self.topFrame, text = 'Add Member', font = 'arial 22 bold', bg = 'white', fg = '#003f8a')
        heading.place(x = 290, y = 60)

        #name
        self.lbl_name = Label(self.bottomFrame, text = 'Name', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_name.place(x = 40, y = 40)
        self.ent_name = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_name.insert(0, 'Enter Name')
        self.ent_name.place(x = 150, y = 45)
        #email
        self.lbl_email = Label(self.bottomFrame, text = 'Email', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_email.place(x = 40, y = 80)
        self.ent_email = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_email.insert(0, 'Enter Email')
        self.ent_email.place(x = 150, y = 85)
        #phone
        self.lbl_phone = Label(self.bottomFrame, text = 'Phone No.', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_phone.place(x = 40, y = 120)
        self.ent_phone = Entry(self.bottomFrame, width = 30, bd = 4)
        self.ent_phone.insert(0, 'Enter Phone No.')
        self.ent_phone.place(x = 150, y = 125)

        #button
        button = Button(self.bottomFrame, text = 'Add Member', command = self.addMember)
        button.place(x = 270, y = 120)

    def addMember(self):
        name = self.ent_name.get()
        email = self.ent_email.get()
        phone = self.ent_phone.get()

        if name and email and phone !='':
            try:
                query = "INSERT INTO 'members' (memberName, memberEmail, memberPhone) VALUES(?,?,?)"
                cur.execute(query, (name, email, phone))
                con.commit()
                messagebox.showinfo('Success', 'Member added successfully', icon = 'info')

            except:
                messagebox.showerror('Error', 'Cannot add data to Database', icon = 'error')


        else:
            messagebox.showerror('Error', 'Please fill all the fields', icon = 'warning')
        
                
