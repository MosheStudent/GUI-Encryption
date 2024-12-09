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

        #output key var
        self.dataKeyLabel = tkinter.Label(text='')

        #Output Label:
        label = tkinter.Label(text="OUTPUT:")
        label.pack()

        #frame to hold text widget and scroll bar:
        frame = tkinter.Frame(self.root)
        frame.pack(padx=10, pady=10, expand=True, fill=tkinter.BOTH)

        #output text widget with screen wrap 
        self.textBox = tkinter.Text(frame, wrap=tkinter.WORD, width=40, height=10)
        self.textBox.pack(side=tkinter.LEFT, padx=0, pady=0, expand=True, fill=tkinter.BOTH)


        #scroll bar:
        self.scrollBar = tkinter.Scrollbar(frame, command=self.textBox.yview)
        self.scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.textBox.config(yscrollcommand=self.scrollBar.set)



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

    def updateOutput(self, output):
        self.textBox.delete("1.0", tkinter.END)
        self.textBox.insert(tkinter.END, output)

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
        error_window.geometry('300x300')

        message = tkinter.Label(error_window, text="Error")
        message.pack()

    def printEncSM(self):
        try:
            #encrypts and prints ceaser cipher
            t  = self.b.enc(self.data)

            self.updateOutput(str(t))
            self.dataKeyLabel.config(text=f'key: {self.b.key}')
            self.dataKeyLabel.pack()

        except:
            self.errorWindow()

    def printEncASM(self):
        try:
        #prints and encryptss rsa cipher
            t = self.a.enc(self.data)

            self.updateOutput(str(t))
            self.dataKeyLabel.config(text=f'key e: {self.a.e}, key n: {self.a.n}, p = {self.a.p}, q = {self.a.q}')
            self.dataKeyLabel.pack()

            self.dataKeyLabel.pack()

        except:
            self.errorWindow()

    def printDecSM(self):
        try:
            t = self.b.dec(self.data, self.key1)

            self.updateOutput(str(t))
            self.dataKeyLabel.config(text=f'key: {self.key1}')
            
            self.dataKeyLabel.pack()

        except:
            self.errorWindow()
         
    def printDecASM(self):
        try:
            t = self.a.dec(str(self.data), int(self.key1), int(self.key2))

            self.updateOutput(str(t))
            self.dataKeyLabel.config(text=f'key: p: {self.key1}, q: {self.key2}')
            
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
        self.root.geometry("600x600")
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

                self.updateOutput(self.data)
            
            except:
                self.errorWindow()

    def exportFiles(self):
        filename = tkinter.filedialog.asksaveasfilename(title='Save as', 
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if filename:
            try:
                f = open(filename, "w")
                f.write(self.textBox.get(1.0, "end-1c"))
                f.close()

            except:
                self.errorWindow()


if __name__ == "__main__":
    r = MainWIn()




    
