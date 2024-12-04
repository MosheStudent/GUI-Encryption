import tkinter
import sym

#sym class init
cipher = sym.Sym()

#calls to sym class
def enc():
    pass

def dec():
    pass


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

#inputButton
button = tkinter.Button(text="Enter", command=funct)
button.pack()

#Output label
text2 = tkinter.Label(root, text="OutPut:")
text2.pack(pady=50)

root.mainloop()