import random


class RSA:
    def __init__(self):
        self.primes = []

        #private data:
        self.q = 0
        self.p = 0

        #Public data:
        self.e = 0
        self.publicKey = 0

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
    def isPrime(num):
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
        self.publicKey = self.p * self.q

    def generateE(self):
        comp = (self.p - 1)(self.q - 1)

        for i in range (2, comp-1):
            if (self.gcd(comp, i) == 1):
                self.e = i
                return

    def enc(self, text):
        pass

    def dec(self, text, q, p):
        pass




    






