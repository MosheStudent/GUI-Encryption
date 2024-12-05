import random

from sympy import mod_inverse


class RSA:

    def __init__(self):

        self.primes = []


        #private data:
        self.q = 0
        self.p = 0


        #Public data:
        self.e = 0
        self.n = 0
        self.PUBLIC_KEY = []

        #initialzing functions
        self.primeGen()
        self.generateE()

    #function returns greatest common divisor of 2 numbers (recursive)

    def gcd(self, max, min):

        if (max % min == 0):

            return min


        r = max % min

        max = min
        min = r


        return self.gcd(max, min)
        
        


    #function to check if prime number

    def isPrime(self, num):

        for i in range(2, num-1):

            if (num % i == 0):

                return False


        return True


    #generates and fills the list with a range of prime numbers

    """The range is relativaly small for encryption, but this

    is a simple school project, 1000 will suffice"""


    def primeGen(self):

        randStart  = random.randint(2, 1000)

        randEnd = random.randint(randStart, randStart + 1000)


        for i in range(randStart, randEnd):

            if (self.isPrime(i)):
                self.primes.append(i)


        self.q = random.choice(self.primes)

        self.p = random.choice(self.primes)
        self.n = self.p * self.q
        self.PUBLIC_KEY.append(self.n)

    #Generates the encryption exponent (public)
    def generateE(self):
        comp = (self.p - 1) * (self.q - 1)


        for i in range (2, comp-1):

            if (self.gcd(comp, i) == 1):
                self.e = i
                self.PUBLIC_KEY.append(self.e)
                return

    #Encodes given text and returns
    def enc(self, text):

        encText = ""


        for char in text:

            encText += str((ord(char) ** self.e) % self.n) + "|"


        return encText
        
        

    #decodes given text with q and p values, and returns
    def dec(self, text, q, p):

        DefChar = ''

        decString = ""


        d = mod_inverse(self.e, ((q-1) * (p-1)))



        for char in text:

            if (char == '|'):

                decString += chr((int(DefChar) ** d ) % self.n) 

                DefChar = ''


            else:

                DefChar += str(char)


        return decString
                


                



