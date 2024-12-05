import sym
import asm

#helper class to decode and encode files from system pc:

class FileSys:
    def __init__(self, file):
        self.file = file

    def encFile(self, en_type):
        if (en_type == "sym"):
            s = sym.Sym()
            print(s.key)

            file = open(self.file, "r")
            encodedFile = s.enc(file.read())
            file.close()

            new_file = open(self.file, "w")
            new_file.write(encodedFile)
            new_file.close()

    def decFile(self, en_type, key):
        if (en_type == "sym"):
            s = sym.Sym()

            file = open(self.file, "r")
            decodedFile = s.dec(file.read(), key)
            file.close()

            new_file = open(self.file, "w")
            new_file.write(decodedFile)
            new_file.close()

