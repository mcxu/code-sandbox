"""
Given array of pos ints representing denominations, and a single non-negative
int representing a target amount of money, implement function that returns
SMALLEST NUMBER OF COINS needed to make change for target amount.

Sample input: 7, [1,5,10]
Sample output: 3 (2x1 + 1x5)
"""

class Prob:
    
    """
    Initial attempt
    Complexity
    Time: 
        outer for loop: j -> denom(d) iterations: O(d)
        inner for loop: i -> d, d-1, d-2, d-3, ... iterations: O(d)
        Total: O(d^2)
    Space:
        O(d) for storage array
    """
    @staticmethod
    def minNumberOfCoinsForChange(n, denoms):
        denoms = sorted(denoms) # O(n*log_2(n)) time
        print("denoms sorted: ", denoms)
        
        # stores results for min number of coins for solution with denoms[i:]
        # where i -> 0 to len(denoms)
        numCoinsForDenom = [float("inf")] * len(denoms) # O(d) space
        
        for j in range(len(denoms)-1, -1, -1):
            print("------ j= %s d[j]= %s" % (j, denoms[j]))
            numCoins = 0
            nCopy = n
            for i in range(j, -1, -1):
                d = denoms[i]
                print("i= %s, d= %s, n= %s" % (i, d, nCopy))
                quo = int(nCopy/d)
                if quo > 0:
                    numCoins += quo
                print("    numCoins=", numCoins)
                nCopy = nCopy%d
                print("    remainder n= %s" % (nCopy))
            
            print("numCoins final: ", numCoins)
            if nCopy == 0: numCoinsForDenom[j] = numCoins
            print("numCoinsForDenom: ", numCoinsForDenom)
        
        minCoins = min(numCoinsForDenom) # O(n) time
        if minCoins == float("inf"): return -1
        else: return minCoins
    
    '''
    Dynamic programming, iterative. Using minWays array to store solns to subproblems.
    Let n=amount, d=len(denoms)
    Time complexity: O(n*d).
    Space complexity: O(n), since mnc stores <= n+1 solns to subproblems.
    '''
    @staticmethod
    def minNumberOfCoinsForChangeDP(n, denoms):
        # init array to store min number of ways
        # Let mnc (min num coins) be an array to store solns to subproblems.)
        mnc = [float("inf") for i in range(n+1)] # O(n) space
        mnc[0] = 0 # if n=0, then there are 0 number of coins needed.
        print("mnc: ", mnc)
        print("initial min in mnc: ", min(mnc))

        for i in range(n+1): # O(n) time
            print("i=", i)
            for j in range(len(denoms)): # O(d) time
                d = denoms[j]
                print(" j= {}, d= {}".format(j,d))
                if i >= d:
                    mnc[i] = min(mnc[i], mnc[i-d] + 1)
                    print("     mnc: ", mnc)
        
        minWaysFinal = mnc[n]
        if minWaysFinal == float("inf"):
            return -1
        else:
            return minWaysFinal

    @staticmethod
    def test1(alg):
        n = 7
        denoms = [1,5,10] 
        numCoins = alg(n, denoms)
        print("test1 numCoins: ", numCoins)
    
    @staticmethod
    def test2(alg):
        n = 0
        denoms = [1,2,3]
        numCoins = alg(n, denoms)
        print("test2 numCoins: ", numCoins)

    @staticmethod
    def test3(alg):
        # this sample input from: https://www.youtube.com/watch?v=HWW-jA6YjHk&t=528s
        # correct ans is 4.
        n = 31
        denoms = [25,10,1] 
        numCoins = alg(n, denoms)
        print("test3 numCoins: ", numCoins)

    @staticmethod
    def test4(alg):
        # correct answer is 2
        n = 135
        denoms = [39, 45, 130, 40, 4, 1, 60, 75]
        numCoins = alg(n, denoms)
        print("test4: num coins: ", numCoins)
    
    @staticmethod
    def test5(alg):
        n = 9
        denoms = [3,5]
        numCoins = alg(n, denoms)
        print("test5: num coins: ", numCoins)


#alg = Prob.minNumberOfCoinsForChange
alg = Prob.minNumberOfCoinsForChangeDP
#Prob.test1(alg)
#Prob.test2(alg)
#Prob.test3(alg)
Prob.test4(alg)
#Prob.test5(alg)
