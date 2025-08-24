from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import sqlite3
import addBook, addMember


con = sqlite3.connect('Libarary.db')
cur = con.cursor()

class Main(object):
    def __init__(self,master):
        self.master = master

        def displayBooks(self):
            books = cur.execute("SELECT * FROM 'books'").fetchall()
            count = 0
            for book in books:
                print(book)
                self.list_books.insert(count,str(book[0])+"-"+book[1])
                count += 1


        #frames
        mainFrame=Frame(self.master)
        mainFrame.pack()
        #top
        topFrame = Frame(mainFrame, width = 1350, height = 70, bg = '#f8f8f8', padx = 20, relief = SUNKEN, borderwidth = 2)
        topFrame.pack(side = TOP, fill = X)
        #centre
        centerFrame = Frame(mainFrame, width = 1350, relief = RIDGE, bg = '#e0f0f0', height = 680)
        centerFrame.pack(side = TOP)
        #left
        centerLeftFrame = Frame(centerFrame, width = 900, height = 700, bg = '#f0f0f0', borderwidth = 2, relief = SUNKEN)
        centerLeftFrame.pack(side = LEFT)
        #right
        centerRightFrame = Frame(centerFrame, width = 450, height = 700, bg = '#e0f0f0', borderwidth = 2, relief = SUNKEN)
        centerRightFrame.pack(side = RIGHT)

        #search
        search_bar = LabelFrame(centerRightFrame, width = 440, height = 75, text = 'search', bg = '#9bc9ff')
        search_bar.pack(fill = BOTH)
        self.lbl_search = Label(search_bar, text = 'Search Book', font = 'arial 12 bold', bg = '#9bc9ff', fg = 'white')
        self.lbl_search.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.ent_search = Entry(search_bar, width = 30, bd = 10)
        self.ent_search.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady = 10)
        self.btn_search = Button(search_bar, text = 'Search', font = 'arial 12', bg = '#fcc324', fg = 'white')
        self.btn_search.grid(row = 0, column = 4, padx = 20, pady = 10)
        #list 
        list_bar = LabelFrame(centerRightFrame, width = 440, height = 175, text = 'list', bg = '#fcc324')
        list_bar.pack(fill = BOTH)
        lbl_list = Label(list_bar, text = 'Sort by', font = 'times 16 bold', fg = '#2488ff', bg = '#fcc324')
        lbl_list.grid(row = 0, column = 2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text = 'All Books', var = self.listChoice, value = 1, bg = '#fcc324')
        rb2 = Radiobutton(list_bar, text = 'Acailable Books', var = self.listChoice, value = 2, bg = '#fcc324')
        rb3 = Radiobutton(list_bar, text = 'Borrowed Books', var = self.listChoice, value = 3, bg = '#fcc324')
        rb1.grid(row = 1, column = 0)
        rb2.grid(row = 1, column = 1)
        rb3.grid(row = 1, column = 2)
        btn_list = Button(list_bar, text = 'List Books', bg = '#2488ff', fg = 'white', font = 'arial 12')
        btn_list.grid(row = 1, column = 3, padx = 40, pady = 10)

        #title
        image_bar = Frame(centerRightFrame, width = 440, height = 350)
        image_bar.pack(fill = BOTH)
        self.title_right = Label(image_bar, text = 'Welcom to our Library', font = 'arial 16 bold')
        self.title_right.grid(row = 0)
        self.img_library = PhotoImage(file = 'icons/library.png')
        self.lblImg = Label(image_bar, image = self.img_library)
        self.lblImg.grid(row = 1)
        #add book
        self.iconbook=PhotoImage(file='icons/addbook.png')
        self.btnbook = Button(topFrame, text = 'Add Book', image = self.iconbook, compound = LEFT, font = 'arial 12 bold', width = 100, height = 40, command = self.addBook)
        self.btnbook.pack(side = LEFT, padx = 10)
        #add member
        self.iconmember = PhotoImage(file = 'icons/users.png')
        self.btnmember = Button(topFrame, text = 'Add Member', font = 'arial 12 bold', padx = 10, width = 100, height = 40, command = self.addMember)
        self.btnmember. configure(image = self.iconmember, compound = LEFT)
        self.btnmember.pack(side = LEFT)
        #give book
        self.icongive=PhotoImage(file = 'icons/givebook.png')
        self.btngive = Button(topFrame, text = 'Give Book', font = 'arial 12 bold', padx = 10, image = self.icongive, compound = LEFT, width = 100, height = 40)
        self.btngive.pack(side = LEFT)

        #tabs
        self.tabs = ttk.Notebook(centerLeftFrame, width = 900, height = 600)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file = 'icons/books.png')
        self.tab2_icon = PhotoImage(file = 'icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text = 'Library Management', image = self.tab1_icon, compound = LEFT)
        self.tabs.add(self.tab2, text = 'Statistics', image = self.tab2_icon, compound = LEFT)

        #list books
        self.list_books = Listbox(self.tab1, width = 40, height = 30, bd = 5, font = 'times 12 bold')
        self.sb = Scrollbar(self.tab1, orient = VERTICAL)
        self.list_books.grid(row = 0, column = 0, padx = (10,0), pady = 10, sticky = N)
        self.sb.config(command = self.list_books.yview)
        self.list_books.config(yscrollcommand = self.sb.set)
        self.sb.grid(row = 0, column = 0, sticky = N+S+E)
        #list details
        self.list_details = Listbox(self.tab1, width = 80, height = 30, bd = 5, font = 'times 12 bold')
        self.list_details.grid(row = 0, column = 1, padx = (10,0), pady = 10, sticky = N)

        #statistics
        self.lbl_book_count = Label(self.tab2, text = '', pady = 20, font = 'verdana 14 bold')
        self.lbl_book_count.grid(row = 0)
        self.lbl_member_count = Label(self.tab2, text = '', pady = 20, font = 'verdana 14 bold')
        self.lbl_member_count.grid(row = 1, sticky = W)
        self.lbl_taken_count = Label(self.tab2, text = '', pady = 20, font = 'verdana 14 bold')
        self.lbl_taken_count.grid(row = 2, sticky = W)
        #functions
        displayBooks(self)

    def addBook(self):
        add = addBook.AddBook()

    def addMember(self):
        member = addMember.AddMember()

def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    try: #ai code
        app_icon = PhotoImage(file='icons/book.png') 
        root.iconphoto(False, app_icon)
    except Exception as e:
        print(f"Failed to load icon: {e}") 
    root.mainloop() #not aicode

if __name__ == '__main__':
    main()