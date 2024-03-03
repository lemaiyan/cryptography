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

        return p, q

if __name__ == "__main__":
    prime = PrimeNumber(2,100)
    p, q = prime.generate_key_pair()
    print(f"Randomly generated prime number p: {p}")
    print(f"Randomly generated prime number q: {q}")