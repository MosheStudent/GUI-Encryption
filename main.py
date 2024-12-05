import tkinter
import sym

#sym class init
cipher = sym.Sym()

#calls to sym class
def enc(msg):
    textval.set(f'{cipher.cipher(msg)} \t key={cipher.key}')

def dec(msg):
    text3 = tkinter.Label(root, text="Enter key: ")
    text3.pack()

    
    inputLine = tkinter.Entry(root)
    inputLine.pack()

    
    def write():
        textval.set(cipher.dec(msg, inputLine.get()))
        button2.destroy()
        inputLine.destroy()
        text3.destroy()



    button2 = tkinter.Button(root, text="Enter", command=write)
    button2.pack()


#window startup
root = tkinter.Tk()
root.geometry("400x400")
header = root.title("Cipher Tool")

#encryption or decryption
choices = ["Encrypt", "Decrypt"]
initVal = tkinter.StringVar(root)
initVal.set(choices[0])
choiceBox = tkinter.OptionMenu(root, initVal, *choices)
choiceBox.pack(pady= 20)

#text label
text1 = tkinter.Label(root, text="Enter message:")
text1.pack(pady=25)

#Input line
entryLine = tkinter.Entry(root)
entryLine.pack(padx=40)

#output label
textval = tkinter.StringVar(root)
outputLine = tkinter.Label(root, textvariable=textval)
outputLine.pack(pady=20)

#directs to decypher or to encrypt
def commandCenter():
    if (initVal.get() == choices[0]):
        enc(entryLine.get())

    else:
        dec(entryLine.get())

#inputButton
button = tkinter.Button(text="Enter", command=commandCenter)
button.pack()


root.mainloop()

#if __name__ == "main"