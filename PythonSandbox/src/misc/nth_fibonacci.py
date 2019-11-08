class Fibonacci:

    def __init__(self):
        # map of fib index to the fib number
        self.fibMap = {}

    # index of 0 is 1
    def getNthFib(self, n):
        #print("n= ", n)
        # count starting from 0
        # if n == 0 or n == 1:
        #     return n
        
        # error check
        if n < 1:
            return 0

        # count starting from 1
        if n == 1 or n == 2:
            return n-1

        return self.getNthFib(n-1)+self.getNthFib(n-2)

    def test_getNthFib(self):
        a = self.getNthFib(6)
        print("a: ", a)


    def getNthFib_memoized(self, n):
        # error check
        if n < 1:
            return 0

        # count starting from 1
        if n == 1 or n == 2:
            return n-1

        if n in self.fibMap.keys():
            #print("n={} in fibMap".format(n))
            return self.fibMap[n]
            
        self.fibMap[n] = self.getNthFib_memoized(n-1)+self.getNthFib_memoized(n-2)
        return self.fibMap[n]

    def test_getNthFib_memoized(self):
        a = self.getNthFib_memoized(100)
        print("a: ", a)

    def test_getNthFib_memoized_multi(self):
        for i in range(0, 101):
            a = self.getNthFib_memoized(i)
            print("ind: {}, fib: {}".format(i, a))

def main():
    f = Fibonacci()
    #f.test_getNthFib()
    #f.test_getNthFib_memoized()
    f.test_getNthFib_memoized_multi()

if __name__ == "__main__":
    main()