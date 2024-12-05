import random

#This class will Use Ceaser cipher encryption:

#CONSTANTS:
MAX_KEY = 126
MIN_KEY = 32
TOTAL_KEYS = 95
NEWLINE = 10

# Ceaser cipher:
class Sym:
    def __init__(self):
        self.key = random.randint(1, TOTAL_KEYS) # Generate ranodom key
    
    # Encode function

    def enc(self, text): 
        ascText = ""

        for c in text:
            if (ord(c) == NEWLINE): #deal with newline case
                ascText += c
  

            else:
                asc = ord(c) + self.key

                if (asc > MAX_KEY):
                    asc = (asc - (MAX_KEY+1)) + MIN_KEY

                ascText += chr(asc)

        return ascText

    # Decode function

    def dec(self, text, key):
        decScript = ""

        for c in text:
            if (ord(c) == NEWLINE): #deal with new line case
                decScript += c
                
            else:

                ret = ord(c) - int(key) 
                if (ret < MIN_KEY):
                    ret += TOTAL_KEYS

                decScript += chr(ret)

        return decScript






    
        

        
