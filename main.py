from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import sqlite3
import addBook, addMember, giveBook
from giveBook import *


con = sqlite3.connect('Libarary.db')
cur = con.cursor()

class Main(object):
    def __init__(self,master):
        self.master = master

        def displayStatistics(evt):
            count_books = cur.execute("SELECT count(bookID) FROM books").fetchall()
            count_members = cur.execute("SELECT count(memberID) FROM members").fetchall()
            taken_books = cur.execute("SELECT count(status) FROM books WHERE status =?", (1,)).fetchall()
            print(count_books)
            self.lbl_book_count.config(text = str(count_books[0][0]) + ' books in library')
            self.lbl_member_count.config(text = str(count_members[0][0]) + ' members')
            self.lbl_taken_count.config(text = str(taken_books[0][0]) + ' books are borrowed')


        def displayBooks(self):
            books = cur.execute("SELECT * FROM 'books'").fetchall()
            count = 0

            self.list_books.delete(0,END)
            for book in books:
                print(book)
                self.list_books.insert(count,str(book[0]) + "-" + book[1])
                count += 1

            def bookInfo(evt):
                if not self.list_books.curselection():
                    return
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE bookID = ?",(id,))
                book_info = book.fetchall()
                print(book_info)
                self.list_details.delete(0,END)
                self.list_details.insert(0,"Book Name " + book_info[0][1])
                self.list_details.insert(1,"Author " + book_info[0][2])
                self.list_details.insert(2,"No. of Pages " + str(book_info[0][3]))
                self.list_details.insert(3, str(book_info[0][4]))
                if book_info[0][5] == 0:
                    self.list_details.insert(4,"Available")
                    self.list_details.itemconfig(4, bg = 'white', fg = 'green')
                    self.list_details.insert(5, "Borrowed by Nobody")
                else:
                    self.list_details.insert(4,"Not Available")
                    self.list_details.itemconfig(4, bg = 'white', fg = 'red')
                    borrow_info = cur.execute("SELECT * FROM borrows WHERE bookID = ?", (id,)).fetchone()
                    print("borrow info ", borrow_info)
                    if borrow_info:
                        print("tt ", borrow_info)
                        member_id = borrow_info[2]
                        member_info = cur.execute("SELECT memberName FROM members WHERE memberID = ?", (member_id,)).fetchone()
                        self.list_details.insert(5, "Borrowed by " + member_info[0])
                    else:
                        self.list_details.insert(5, "Unavailible")

            def doubleClick(evt):
                global given_id
                value = str(self.list_books.get(self.list_books.curselection()))
                given_id = value.split('-')[0]
                give_book = GiveBook(given_id)

            self.list_books.bind('<<ListboxSelect>>', bookInfo)
            self.tabs.bind('<<NotebookTabChanged>>', displayStatistics)
            #self.tabs.bind('<ButtonRelease-1>', displayBooks)
            self.list_books.bind('<Double-Button-1>', doubleClick)

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
        self.ent_search = Entry(search_bar, width = 20, bd = 10)
        self.ent_search.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)
        self.btn_search = Button(search_bar, text = 'Search', font = 'arial 12', bg = '#fcc324', fg = 'white', command = self.searchBooks)
        self.btn_search.grid(row = 0, column = 3, padx = 20, pady = 10)
        #list 
        list_bar = LabelFrame(centerRightFrame, width = 440, height = 175, text = 'list', bg = '#fcc324')
        list_bar.pack(fill = BOTH)
        lbl_list = Label(list_bar, text = 'Sort by', font = 'times 16 bold', fg = '#2488ff', bg = '#fcc324')
        lbl_list.grid(row = 0, column = 2, columnspan = 2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text = 'All Books', var = self.listChoice, value = 1, bg = '#fcc324')
        rb2 = Radiobutton(list_bar, text = 'Available Books', var = self.listChoice, value = 2, bg = '#fcc324')
        rb3 = Radiobutton(list_bar, text = 'Borrowed Books', var = self.listChoice, value = 3, bg = '#fcc324')
        rb1.grid(row = 1, column = 0)
        rb2.grid(row = 1, column = 1)
        rb3.grid(row = 1, column = 2)
        btn_list = Button(list_bar, text = 'List Books', bg = '#2488ff', fg = 'white', font = 'arial 12', command = self.listBooks)
        btn_list.grid(row = 1, column = 3, padx = 40, pady = 10)
        #title
        image_bar = Frame(centerRightFrame, width = 440, height = 350)
        image_bar.pack(fill = BOTH)
        self.title_right = Label(image_bar, text = 'Welcome to our Library', font = 'arial 16 bold')
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
        #return book
        self.icongive=PhotoImage(file = 'icons/returnbook.png')
        self.btngive = Button(topFrame, text = 'Return Book', font = 'arial 12 bold', padx = 10, image = self.icongive, compound = LEFT, width = 100, height = 40)
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
        displayStatistics(self)

    def addBook(self):
        add = addBook.AddBook()

    def addMember(self):
        member = addMember.AddMember()

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE bookName LIKE ?", ('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0]) + "-" + book[1])
            count += 1
    
    def listBooks(self):
        value = self.listChoice.get()
        if value == 1:
            allbooks = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in allbooks:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
                
        elif value == 2:
            books_in_library = cur.execute("SELECT * From books WHERE status =?", (0,)).fetchall()
            self.list_books.delete(0,END)
            
            count = 0
            for book in books_in_library:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
        else:
            taken_books = cur.execute("SELECT * FROM books WHERE status =?", (1,)).fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in taken_books:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
    #def open_give_book(self):
     #   GiveBook()


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