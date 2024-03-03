import math
import random

class PrimeNumber:
    def __init__(self, lower_limit=2, upper_limt=1000) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limt
    

    def is_prime(self, num):
        prime = True
        if num == 1:
            prime = False
        elif num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # if factor is found, set prime to False
                    prime = False
                    # break out of loop
                    break
        return prime

    def generate_prime_number(self, start, end):
        while True:
            num = random.randint(start, end)
            if self.is_prime(num):
                return num

    def generate_key_pair(self):
        # Generate two prime numbers
        p = self.generate_prime_number(self.lower_limit, self.upper_limit)
        q = self.generate_prime_number(self.lower_limit, self.upper_limit)
        print(f"Randomly generated prime number p: {p}")
        print(f"Randomly generated prime number q: {q}")
        return p, q
    
class RSA(PrimeNumber):
    def __init__(self, lower_limit=2, upper_limt=1000) -> None:
        super().__init__(lower_limit, upper_limt)
        self.p, self.q = super().generate_key_pair()
        self.n = self.__compute_n()
        self.phi = self.__compute_phi()
        self.e = self.__compute_e()
    
    def  __compute_n(self):
        n = self.p * self.q
        print(f"Computed value of n: {n}")
        return n
    
    def __compute_phi(self):
        phi = (self.p - 1) * (self.q - 1)
        print(f"Computed value of phi: {phi}")
        return phi
    
    def __compute_e(self):
        e = random.randint(2, self.phi)
        while(e<self.phi):
            if (math.gcd(e, self.phi) == 1):
                break
            else:
                e = random.randint(2, self.phi)
        
        print(f"Computed value of e: {e}")
        return e
    
    def __compute_d(self):
        d = 0
        while (d * self.e) % self.phi != 1:
            d += 1
        print(f"Computed value of d: {d}")
        return d
    
    def __get_public_key(self):
        print(f"Public key {self.e, self.n}:")
        return self.e, self.n
    
    def get_private_key(self):
        d = self.__compute_d()
        print(f"Private key {d, self.n}")
        return d, self.n
    
    def encrypt(self, message):
        e, n = self.__get_public_key()
        C = (message ** e) % n
        print(f"Encrypted message: {C}")
        return C
    
    def decrypt(self, encrypted_message):
        d, n = self.get_private_key()
        M = (encrypted_message ** d) % n
        print(f"Decrypted message: {M}")
        return M

if __name__ == "__main__":
    rsa = RSA(2, 1000)
    message = int(input("Enter the message to be encrypted: "))
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)
    assert message == decrypted_message