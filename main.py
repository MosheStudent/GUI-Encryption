import tkinter
from tkinter import filedialog

import sym
import asm
import fileSys



class MainWIn:
    def __init__(self):
        self.root = tkinter.Tk()
        self.encTypes = ["CEASER", "RSA"]
        self.convTypes = ["ENCRYPT", "DECRYPT"]
        
        #window Setup Funcs
        self.winSetup()
        self.menuSetup()
        self.encryptionType()
        self.encrypt_or_decrypt()
        self.enterBox()
        self.keyBox()
        self.enterButton()

        self.root.mainloop()

    def encryptionType(self):
        #asm or sym
        optionVar = tkinter.StringVar(self.root)
        optionVar.set(self.encTypes[0])
        dropdown = tkinter.OptionMenu(self.root, optionVar, *self.encTypes)
        dropdown.pack()

    def encrypt_or_decrypt(self):
        #dropdown for encryption or decryption:
        optionVar = tkinter.StringVar(self.root)
        optionVar.set(self.convTypes[0])
        dropdown = tkinter.OptionMenu(self.root, optionVar, *self.convTypes)
        dropdown.pack()

    def enterBox(self):
        #enter box for data:
        label = tkinter.Label(text="Enter data:")
        label.pack()

        box = tkinter.Entry()
        box.pack()

    def keyBox(self):
        #key enter fields
        label = tkinter.Label(text="Key (only for decryption):")
        label.pack()

        box1 = tkinter.Entry()
        box2 = tkinter.Entry()

        box1.pack()
        box2.pack()

    def enterButton(self):
        button = tkinter.Button(text="enter")
        button.pack()
        

    def winSetup(self):
        #Basic window init:
        self.root.geometry("400x400")
        self.root.title("Encryption")

    def menuSetup(self):
        #menu:
        menu = tkinter.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tkinter.Menu(menu)

        helpMenu = tkinter.Menu(menu)

        menu.add_cascade(label='File', menu=filemenu)
        menu.add_cascade(label='Help', menu=helpMenu)

        helpMenu.add_command(label='About', command=self.readMe)
        filemenu.add_command(label='Import', command=self.browseFiles)
        filemenu.add_command(label='Export', command=self.browseFiles)

    def readMe(self):
        new_window = tkinter.Toplevel(self.root)
        new_window.title("About")
        new_window.geometry("400x400")

        newFile = open("about.txt", 'r')
        AboutLabel = tkinter.Label(new_window, text=newFile.read())
        AboutLabel.pack()
        newFile.close()


    #Open file explorer for file import
    def browseFiles(self):
        filename = tkinter.filedialog.askopenfilename(initialdir = "/",
        title = "Select a File",
        filetypes = (("Text files","*.txt*"),("all files", "*.*")))


r = MainWIn()




    
