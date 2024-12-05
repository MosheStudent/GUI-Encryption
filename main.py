import tkinter
from tkinter import filedialog

import sym
import asm
import fileSys



class MainWIn:
    def __init__(self):
        self.root = tkinter.Tk()
        self.encTypes = ["CEASER", "RSA"]
        
        #window Setup Funcs
        self.winSetup()
        self.menuSetup()
        self.encryptionType()

        self.root.mainloop()

    def encryptionType(self):
        #asm or sym
        optionVar = tkinter.StringVar(self.root)
        optionVar.set(self.encTypes[0])
        dropdown = tkinter.OptionMenu(self.root, optionVar, *self.encTypes)
        dropdown.pack()
        

    def winSetup(self):
        #Basic window init:
        self.root.geometry("400x400")
        self.root.title("Encryption")

    def menuSetup(self):
        #menu:
        menu = tkinter.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tkinter.Menu(menu)

        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Import', command=self.browseFiles)

    #Open file explorer for file import
    def browseFiles(self):
        filename = tkinter.filedialog.askopenfilename(initialdir = "/",
        title = "Select a File",
        filetypes = (("Text files","*.txt*"),("all files", "*.*")))


r = MainWIn()




    
