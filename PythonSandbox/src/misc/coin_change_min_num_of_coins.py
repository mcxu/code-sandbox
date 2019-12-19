"""
Given array of pos ints representing denominations, and a single non-negative
int representing a target amount of money, implement function that returns
smallest number of coins needed to make change for target amount.

Sample input: 7, [1,5,10]
Sample output: 3 (2x1 + 1x5)
"""

class Prob:
    
    """
    Initial attempt
    Complexity
    Time: 
        outer for loop: j -> denom(d) iterations: O(d)
        inner for loop: i -> d, d-1, d-2, d-3, ... iterations: O(lg(d))
        get min value from array: O(d), since array is size d
        O(d)*O(lg(d)) + O(d) = O(d)*[O(lg(d)) + 1] = O(d * lg(d))
    Space:
        O(d) for storage array
    """
    @staticmethod
    def minNumberOfCoinsForChange(n, denoms):
        denoms = sorted(denoms)
        print("denoms sorted: ", denoms)
        
        # stores results for min number of coins for solution with denoms[i:]
        # where i -> 0 to len(denoms)
        numCoinsForDenom = [float("inf")] * len(denoms)
        
        for j in range(len(denoms)-1, -1, -1):
            print("------ j= %s d[j]= %s" % (j, denoms[j]))
            numCoins = 0
            nCopy = n
            rdr = 0
            for i in range(len(denoms[:j]), -1, -1):
                d = denoms[i]
                print("i= %s, d= %s, n= %s" % (i, d, nCopy))
                quo = int(nCopy/d)
                if quo > 0:
                    numCoins += quo
                print("    numCoins=", numCoins)
                rdr = nCopy%d
                print("    quo: %s, rdr %s" % (quo, rdr))
                nCopy = rdr
                print("    n=rdr= %s" % (nCopy))
            
            print("numCoins final: ", numCoins)
            if rdr == 0: numCoinsForDenom[j] = numCoins
            print("numCoinsForDenom: ", numCoinsForDenom)
        
        minCoins = min(numCoinsForDenom)
        if minCoins == float("inf"): return -1
        else: return minCoins
        
    @staticmethod
    def test1():
        n = 7
        denoms = [1,5,10]
        Prob.minNumberOfCoinsForChange(n, denoms)
    
    @staticmethod
    def test2():
        n = 0
        denoms = [1,2,3]
        Prob.minNumberOfCoinsForChange(n, denoms)

    @staticmethod
    def test3():
        n = 4
        denoms = [1,5,10]
        Prob.minNumberOfCoinsForChange(n, denoms)

    @staticmethod
    def test4():
        # correct answer is 2
        n = 135
        denoms = [39, 45, 130, 40, 4, 1, 60, 75]
        nc = Prob.minNumberOfCoinsForChange(n, denoms)
        print("test4: num coins: ", nc)
    
    @staticmethod
    def test5():
        n = 9
        denoms = [3,5]
        nc = Prob.minNumberOfCoinsForChange(n, denoms)
        print("test5: num coins: ", nc)

#Prob.test1()
#Prob.test2()
#Prob.test3()
#Prob.test4()
Prob.test5()

