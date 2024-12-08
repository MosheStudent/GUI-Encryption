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

        #output text var
        self.dataLabel = tkinter.Label(text='')
        self.dataKeyLabel = tkinter.Label(text='')

        #input from entry fields:
        self.box = tkinter.Entry()
        self.data = ''

        #input keys:
        self.box1 = tkinter.Entry()
        self.box2 = tkinter.Entry()
        self.key1 = ''
        self.key2 = ''

        #import/export
        self.Import = False

        #window Setup Funcs
        self.winSetup()
        self.menuSetup()
        self.encryptionType()
        self.encrypt_or_decrypt()
        self.enterBox()
        self.keyBox()
        self.enterButton()

        #update key button:
        self.updateKeyButton()

        #enc objects:
        self.a = asm.RSA()

        self.b = sym.Sym()


        #main loop run:
        self.root.mainloop()

    def updateKey(self):
        if (self.sysVar.get() == "CEASER"):
            self.b = sym.Sym()

            self.dataKeyLabel.config(text=self.b.key)
            self.dataKeyLabel.pack()

        
        else:
            self.a = asm.RSA()
            self.dataKeyLabel.config(text=self.a.n)
            self.dataKeyLabel.pack()

    def updateKeyButton(self):
        button = tkinter.Button(text="Update Keys", command=self.updateKey)
        button.pack()

    def errorWindow(self):
        error_window = tkinter.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry('100x100')

        message = tkinter.Label(error_window, text="Error")
        message.pack()

    def printEncSM(self):
        try:
            #encrypts and prints ceaser cipher
            t  = self.b.enc(self.data)

            self.dataLabel.config(text=t)
            self.dataKeyLabel.config(text=f'key: {self.b.key}')

            self.dataKeyLabel.pack()
            self.dataLabel.pack()

        except:
            self.errorWindow()

    def printEncASM(self):
        #try:
            #prints and encryptss rsa cipher
        t = self.a.enc(self.data)

        self.dataLabel.config(text=t)
        self.dataKeyLabel.config(text=f'key e: {self.a.e}, key n: {self.a.n}')

        self.dataKeyLabel.pack()
        self.dataLabel.pack()

        print (self.a.p)
        print(self.a.q)


        #except:
            #self.errorWindow()

    def printDecSM(self):
        try:
            t = self.b.dec(self.data, self.key1)

            self.dataLabel.config(text=t)
            self.dataKeyLabel.config(text=f'key: {self.key1}')
            
            self.dataLabel.pack()
            self.dataKeyLabel.pack()

        except:
            self.errorWindow()
         
    def printDecASM(self):
        try:
            t = self.a.dec(str(self.data), int(self.key1), int(self.key2))

            self.dataLabel.config(text=t)
            self.dataKeyLabel.config(text=f'key: p: {self.key1}, q: {self.key2}')
            
            self.dataLabel.pack()
            self.dataKeyLabel.pack()
            
        except:
            self.errorWindow()



    def controlCenter(self):
        #updates entry fields to variable
        if (self.Import == False or self.box.get() != ''):
            self.data = self.box.get()

        self.key1 = self.box1.get()
        self.key2 = self.box2.get()

        if (str(self.sysVar.get()) == self.encTypes[0]):
            if (str(self.convVar.get()) == self.convTypes[0]):
                self.printEncSM()
            else:
                self.printDecSM()
        else:
            if (str(self.convVar.get()) == self.convTypes[0]):
                self.printEncASM()
            else:
                self.printDecASM()
            

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
        filemenu.add_command(label='Export', command=self.exportFiles)

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

        if filename:
            try:
                file = open(filename, "r")
                self.data = file.read()
                file.close()

                if (self.box.get() == ''):
                    self.Import = True
            
            except:
                self.errorWindow()

    def exportFiles(self):
        filename = tkinter.filedialog.asksaveasfilename(title='Save as', 
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if filename:
            try:
                f = open(filename, "w")
                f.write(self.dataLabel.cget("text"))
                f.close()

            except:
                self.errorWindow()

r = MainWIn()




    
