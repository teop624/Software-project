from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

class Main(object):
    def __init__(self,master):
        self.master = master

        #frames
        mainFrame=Frame(self.master)
        mainFrame.pack()
        #top
        topFrame = Frame(mainFrame, width = 1350, height = 70, bg = '#f8f8f8', padx = 20, relief = SUNKEN, borderwidth = 2)
        topFrame.pack(side = TOP, fill = X)
        #centre
        centerFrame = Frame(mainFrame, width = 1350, relief = RIDGE, bg = '#e0f0f0', height = 680)
        centerFrame.pack(side = TOP, fill = BOTH, expand = True)
        #left
        centerLeftFrame = Frame(centerFrame, width = 900, height = 700, bg = '#f0f0f0', borderwidth = 2, relief = SUNKEN)
        centerLeftFrame.pack(side = LEFT)
        #right
        centerRightFrame = Frame(centerFrame, width = 450, height = 700, bg = '#e0f0f0', borderwidth = 2, relief = SUNKEN)
        centerRightFrame.pack(side = RIGHT)

        #search
        search_bar = LabelFrame(centerRightFrame, width = 440, height = 175, text = 'search', bg = '#9bc9ff')
        search_bar.pack(fill = BOTH)
        #list 
        list_bar = LabelFrame(centerRightFrame, width = 440, height = 175, text = 'list', bg = '#fcc324')
        list_bar.pack(fill = BOTH)
        #add book
        self.iconbook=PhotoImage(file='icons/addbook.png')
        self.btnbook = Button(topFrame, text = 'Add Book', image = self.iconbook, compound = LEFT, font = 'arial 12 bold')
        self.btnbook.pack(side = LEFT, padx = 10)
        #add member
        self.iconmember = PhotoImage(file = 'icons/users.png')
        self.btnmember = Button(topFrame, text = 'Add Member', font = 'arial 12 bold', padx = 10)
        self.btnmember. configure(image = self.iconmember, compound = LEFT)
        self.btnmember.pack(side = LEFT)
        #give book
        self.icongive=PhotoImage(file = 'icons/givebook.png')
        self.btngive = Button(topFrame, text = 'Give Book', font = 'arial 12 bold', padx = 10, image = self.icongive)
        self.btngive.pack(side = LEFT)



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