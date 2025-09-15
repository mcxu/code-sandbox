class Prime:
    # Is a number prime?
    def isPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def test_isPrime(self):
        n = 5
        res = self.isPrime(n)
        # print("res: ", res)
    
    # Get all prime numbers up to and including n
    def getPrimes(self, n):
        primes = []
        for i in range(2, n+1):
            if self.isPrime(i):
                primes.append(i)
        return primes
    
    def test_getPrimes(self):
        n = 1000
        res = self.getPrimes(n)
        # print("res: ", res)

p = Prime()
# p.test_isPrime()
p.test_getPrimes()
