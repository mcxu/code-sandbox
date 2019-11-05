import random

class NumberUtils:
    @staticmethod
    def generateRandomNumbers(lo, hi, quantity, allowDuplicates=True):
        out = []
        
        if allowDuplicates == False:
            # error check
            if quantity > (hi-lo+1):
                return out
            out = set()
        
        while len(out) != quantity:
            rn = random.randint(lo, hi)
            
            if allowDuplicates:
                out.append(rn)
            else:
                out.add(rn)
        
        if isinstance(out, list):
            return out
        else:
            return list(out)
            
                
    def test1(self):
        a = self.generateRandomNumbers(0, 10, 11, allowDuplicates=False)
        a = sorted(a)
        print(a)
        print("a size: ", len(a))
        
    def test2(self):
        a = self.generateRandomNumbers(0, 10000, 1000, allowDuplicates=False)
        a = sorted(a)
        print(a)
        print("a size: ", len(a))
         
def main():
    nutils = NumberUtils()
    #nutils.test1()
    nutils.test2()

if __name__ == "__main__":
    main()
        