"""
Given array of pos ints representing denominations, and a single non-negative
int representing a target amount of money, implement function that returns
SMALLEST NUMBER OF COINS needed to make change for target amount.

Sample input: 7, [1,5,10]
Sample output: 3 (2x1 + 1x5)
"""

class Prob:
    
    @staticmethod
    def minNumOfCoinsForChangeRec(n, denoms):
        
        def helper(n, denoms):
            
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            
    
    '''
    Dynamic programming, iterative. Using minWays array to store solns to subproblems.
    Let n=amount, d=len(denoms)
    Time complexity: O(n*d).
    Space complexity: O(n), since mnc stores <= n+1 solns to subproblems.
    '''
    @staticmethod
    def minNumOfCoinsForChangeDP(n, denoms):
        denoms = sorted(denoms)
        
        # init array to store min number of ways
        # Let mnc (min num coins) be an array to store solns to subproblems.)
        mnc = [float("inf") for i in range(n+1)] # O(n) space
        mnc[0] = 0 # if n=0, then there are 0 number of coins needed.
        print("initial min in mnc: ", min(mnc))

        for i in range(n+1): # O(n) time
            #print("i=", i)
            for d in range(len(denoms)): # O(d) time
                denom = denoms[d]
                #print(" d= {}, denom= {}".format(d,denom))
                if i >= denom:
                    mnc[i] = min(mnc[i], mnc[i-denom] + 1)
                    #print("     mnc: ", mnc)
                else:
                    break
        print("mnc: ", mnc)
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

    @staticmethod
    def test6(alg):
        n = 6249
        denoms = [186,419,83,408]
        numCoins = alg(n, denoms)
        print("test6: num coins: ", numCoins)

alg = Prob.minNumOfCoinsForChangeDP
#Prob.test1(alg)
#Prob.test2(alg)
#Prob.test3(alg)
#Prob.test4(alg)
#Prob.test5(alg)
Prob.test6(alg)
