import random

class NumberUtils:
    
    # returns: [negative nums],[positive nums]
    @staticmethod
    def isolateNegatives(array):
        negNums = []
        i=0
        while i < len(array):
            #print("i={}, v={}".format(i,array[i]))
            if array[i] < 0:
                negNums.append(array.pop(i))
                i -= 1
            i += 1
        # negative list, positive list
        return negNums, array
    
    @staticmethod
    def test_isolateNegatives():
        a = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
        result = NumberUtils.isolateNegatives(a)
        print("test_isolateNegatives:", result)
    
    @staticmethod
    def getHighestVal(array):
        hi = array[0]
        for i in range(1,len(array)):
            val = array[i]
            if val > hi:
                hi = val
        return hi
    
    @staticmethod                
    def test_getHighestVal():
        l = [5,7,3,5,4,102,7,1,7,9,87,3,5,7,2,23,65,12]
        hi = NumberUtils.getHighestVal(l)
        print("highest val: ", hi)
    
    @staticmethod
    def generateRandomNumbers(lo, hi, quantity, allowDuplicates=True):
        out = []
        
        if allowDuplicates == False:
            # error check
            if quantity > (hi-lo+1):
                return out
            out = set()
        
        while len(out) < quantity:
            rn = random.randint(lo, hi)
            
            if allowDuplicates:
                out.append(rn)
            else:
                out.add(rn)
        
        if isinstance(out, list):
            return out
        else:
            return list(out)
            
    @staticmethod
    def test_generateRandomNumbers1():
        a = NumberUtils.generateRandomNumbers(0, 10, 11, allowDuplicates=False)
        a = sorted(a)
        print(a)
        print("a size: ", len(a))
        
    @staticmethod   
    def test_generateRandomNumbers2():
        a = NumberUtils.generateRandomNumbers(0, 10000, 1000, allowDuplicates=False)
        a = sorted(a)
        print(a)
        print("a size: ", len(a))
    
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*NumberUtils.factorial(n-1)
    
    @staticmethod
    def test_factorial():
        ans = NumberUtils.factorial(5)
        print("factorial: ", ans)
    
    # is n a prime number
    @staticmethod
    def isPrime(n):
        if n <= 1:
            return False
        
        for i in range(1, n+1):
            #print("i= ", i)
            if n % i == 0:
                if i != 1 and i != n:
                    return False

        return True
    
    @staticmethod
    def test_isPrime():
        ns = [i for i in range(21)]
        for n in ns:
            p = NumberUtils.isPrime(n)
            print("n: {}, p: {}".format(n,p))
        

    @staticmethod
    def getPowerset(nums):
        powerset = set([()])
        for n in nums:
            tempset = set()
            for subset in powerset:
                newSubset = subset + tuple([n])
                tempset.add(newSubset)
        
            powerset |= tempset # set union operator
            #powerset.update(tempset) # same as union
        return powerset

    @staticmethod
    def test_getPowerset():
        nums = [1,5,3,6]
        ps = NumberUtils.getPowerset(nums)
        print("res: ", ps)

def main():
    #nutils.test_generateRandomNumbers1()
    #nutils.test_generateRandomNumbers2()
    #nutils.test_getHighestVal()
    #nutils.test_factorial()
    # NumberUtils.test_isPrime()
    NumberUtils.test_getPowerset()

if __name__ == "__main__":
    main()
        