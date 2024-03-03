import random

class PrimeNumber:
    def __init__(self, lower_limit=1, upper_limt=1000) -> None:
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
    
class EulerTotient(PrimeNumber):
    def __init__(self, lower_limit=2, upper_limt=1000) -> None:
        super().__init__(lower_limit, upper_limt)
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def euler_totient_function(self, n):
        count = 0
        for i in range(1, n + 1):
            if self.gcd(n, i) == 1:
                count += 1
        return count

    def generate_euler_totient_values(self, lower_limit, upper_limit):
        for num in range(lower_limit, upper_limit + 1):
            phi_value = self.euler_totient_function(num)
            print(f"Euler Totient Function value for {num}: {phi_value}")


if __name__ == "__main__":
    euler = EulerTotient(1,20)
    p, q = euler.generate_key_pair()
    print(f"Randomly generated prime number p: {p}")
    print(f"Randomly generated prime number q: {q}")
    if p > q:
        p, q = q, p
    euler.generate_euler_totient_values(p, q)