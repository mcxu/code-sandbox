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
    def getHighestVal(array):
        hi = array[0]
        for i in range(1,len(array)):
            val = array[i]
            if val > hi:
                hi = val
        return hi
    
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
    def test_isolateNegatives():
        a = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
        result = NumberUtils.isolateNegatives(a)
        print("test_isolateNegatives:", result)
                    
    def test_getHighestVal(self):
        l = [5,7,3,5,4,102,7,1,7,9,87,3,5,7,2,23,65,12]
        hi = NumberUtils.getHighestVal(l)
        print("highest val: ", hi)
        
    def test_generateRandomNumbers1(self):
        a = self.generateRandomNumbers(0, 10, 11, allowDuplicates=False)
        a = sorted(a)
        print(a)
        print("a size: ", len(a))
        
    def test_generateRandomNumbers2(self):
        a = self.generateRandomNumbers(0, 10000, 1000, allowDuplicates=False)
        a = sorted(a)
        print(a)
        print("a size: ", len(a))
         
def main():
    nutils = NumberUtils()
    #nutils.test_generateRandomNumbers1()
    #nutils.test_generateRandomNumbers2()
    nutils.test_getHighestVal()


if __name__ == "__main__":
    main()
        