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

        #selected encType
        self.sysVar = tkinter.StringVar(self.root)
        self.sysVar.set(self.encTypes[0])

        #selected convType
        self.convVar = tkinter.StringVar(self.root)
        self.convVar.set(self.convTypes[0])

        #input from entry fields:
        self.box = tkinter.Entry()
        self.data = ''

        #input keys:
        self.box1 = tkinter.Entry()
        self.box2 = tkinter.Entry()
        self.key1 = ''
        self.key2 = ''


        #window Setup Funcs
        self.winSetup()
        self.menuSetup()
        self.encryptionType()
        self.encrypt_or_decrypt()
        self.enterBox()
        self.keyBox()
        self.enterButton()

        self.root.mainloop()

    def printEnc(self):
        s = sym.Sym()
        t  = s.enc(self.data)

        l = tkinter.Label(text=t)
        l.pack()

        l2 = tkinter.Label(text=f'key: {s.key}')
        l2.pack()

    def controlCenter(self):
        #updates entry fields to variable
        self.data = self.box.get()
        self.key1 = self.box1.get()
        self.key2 = self.box2.get()

        if (str(self.sysVar.get()) == self.encTypes[0]):
            if (str(self.convVar.get()) == self.convTypes[0]):
                self.printEnc()
        else:
            pass

    def encryptionType(self):
        #asm or sym
        dropdown = tkinter.OptionMenu(self.root, self.sysVar, *self.encTypes)
        dropdown.pack()

    def encrypt_or_decrypt(self):
        #dropdown for encryption or decryption:
        dropdown = tkinter.OptionMenu(self.root, self.convVar, *self.convTypes)
        dropdown.pack()

    def enterBox(self):
        #enter box for data:
        label = tkinter.Label(text="Enter data:")
        label.pack()

        self.box.pack()

    def keyBox(self):
        #key enter fields
        label = tkinter.Label(text="Key (only for decryption):")
        label.pack()

        self.box1.pack()
        self.box2.pack()

    def enterButton(self):
        button = tkinter.Button(text="enter", command=self.controlCenter)
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




    
