import random

class Sym:
    def __init__(self, text, cType):
        self.key = random.randint(1, 26)
        self.text = text
        self.cType = cType

    def cipher(self): # Ceaser cipher:
        ascText = ""

        for c in self.text:
            asc = ord(c) + self.key
            
            if (asc > 126):
                asc -= 126
            
            if (asc < 33):
                asc 


            ascText += chr(asc)

        print (ascText)
        return ascText
    
    def dec(self, text):
        decScript = ""

        for c in text:
            decScript += chr(ord(c) - self.key)
        print (decScript)

33-126
    
    
i = input("> ")
c = Sym(i, 4)

e = c.cipher()
c.dec(e)


#33-126 ascii



    
        

        
