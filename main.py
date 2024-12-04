import tkinter

encType = ["Symmetry", "Asymmetry"]

root = tkinter.Tk()
root.geometry("400x400")
root.title("Encryption")


text = tkinter.Label(root, text="Encryption method: ")
text.pack()

typeBox = tkinter.OptionMenu(root, tkinter.StringVar(root), *encType)
typeBox.pack()

text2 = tkinter.Label(root, text="Enter text:")
text2.pack()

inputText = tkinter.Entry(root)
inputText.pack()

text3 = tkinter.Label(root, text = "The Encrypted text:")
text3.pack()

root.mainloop()

