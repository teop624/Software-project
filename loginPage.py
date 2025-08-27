from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib
from main import Main 

con = sqlite3.connect('Libarary.db')
cur = con.cursor()

def decrypt_data(data, key):
    decrypted = ''
    for char in data:
        decrypted += chr(ord(char) ^ key)
    return decrypted

def encrypt_data(data, key):
    encrypted = ''
    for char in data:
        encrypted += chr(ord(char) ^ key)
    return encrypted

class LoginPage(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry("1350x750+350+200")
        self.title("Employee Login")
        self.resizable(False, False)

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
        heading = Label(self.topFrame, text = 'Employee Login', font = 'arial 22 bold', bg = 'white', fg = '#003f8a')
        heading.place(x = 500, y = 200)

        #username
        self.lbl_username = Label(self.bottomFrame, text = 'Username', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_username.place(x = 500, y = 200)
        self.ent_username = Entry(self.bottomFrame, width = 30, bd = 4)
        #self.ent_username.insert(0, 'Enter Username')

        self.ent_username.insert(0, 'greg')

        self.ent_username.place(x = 550, y = 305)
        #password
        self.lbl_password = Label(self.bottomFrame, text = 'Password', font = 'arial 15 bold', bg = '#fcc324', fg = 'white')
        self.lbl_password.place(x = 400, y = 350)
        self.ent_password = Entry(self.bottomFrame, show = '*', width = 30, bd = 4)
        #self.ent_password.insert(0, 'Enter Password')

        self.ent_password.insert(0, 'paul')

        self.ent_password.place(x = 550, y = 355)
        
        #button
        button = Button(self.bottomFrame, text = 'Login', command = self.login)
        button.place(x = 600, y = 400)


    def login(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        
        if not (username and password):
            messagebox.showerror("Error", "Please enter username and password.", icon = 'warning')
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        username_hash = hashlib.sha256(username.encode()).hexdigest()
        user = cur.execute("SELECT employee, password, memberName FROM members WHERE username = ?", (username_hash,)).fetchone()
        
        if user and user[0] == 1 and user[1] == password_hash:
            name = decrypt_data(user[2], 123)
            messagebox.showinfo("Success", "Welcome " + name + "!", icon = 'info')
            self.master.withdraw()
            self.main_window = Main(self.master, self, name)
            

            
        else:
            messagebox.showerror("Error", "Invalid username or password or you are not an employee.", icon = 'warning')

if __name__ == '__main__':
    root = Tk()
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.withdraw()
    app_icon = PhotoImage(file = 'icons/book.png')
    root.iconphoto(False, app_icon)
    login_app = LoginPage(root)
    root.mainloop()