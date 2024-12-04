import random

class Sym:
    def __init__(self):
        self.key = random.randint(1, 93)

    def cipher(self, text): # Ceaser cipher:
        ascText = ""

        for c in text:
            asc = ord(c) + self.key

            if (asc > 126):
                asc = (asc - 127) + 33

            ascText += chr(asc)

        return ascText
    
    def dec(self, text):
        decScript = ""

        for c in text:
            ret = ord(c) - self.key

            if (ret < 32):
                ret += 94

            decScript += chr(ret)
            
        return decScript

    




    
        

        
