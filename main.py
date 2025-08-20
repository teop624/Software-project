from tkinter import *
from tkinter import ttk

class Main(object):
    def __init__(self,master):
        self.master = master


def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('icons/book.png')
    root.mainloop()

if __name__ == '__main__':
    main()