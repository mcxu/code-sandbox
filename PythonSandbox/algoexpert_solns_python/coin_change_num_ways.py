"""
Given array of pos ints representing denominations, and a single non-negative
int representing a target amount of money. Write function to return number
of ways to make change for that target amount.

Sample input: 6,[1,5]
Sample output: 2 (1x1 + 1x5 and 6x1)
"""

class Prob:
    '''
    Recursive, brute force.
    Let n = starting amount from which to make change.
    Time complexity: O(2^n), since each helper call creates 2 other helper calls.
    Space complexity: O(n), since there at most n recursive calls on the call stack.
    https://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
    '''
    @staticmethod
    def numWaysMakeChangeRec(n, denoms):
        
        def helper(n, denoms, d):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            # If there are no denominations left, there are no ways to make change.
            if d < 0:
                return 0
            
            # solution that contain at least 1 denoms[d] denomination
            # d is passed into helper again b/c there could be another denom[d] that is selected.
            nwWithDenom = helper(n-denoms[d], denoms, d)
            
            # solution that doesn't contain denoms[d] denomination
            # d-1 is passed into helper b/c on the next call, d cannot be chosen.
            nwWithoutDenom = helper(n, denoms, d-1)
            
            return nwWithDenom + nwWithoutDenom
    
        return helper(n, denoms, len(denoms)-1)
    
    '''
    Time complexity: O(n), since for each helper call, there is a (1) previously solved memoized solution that is returned.
    Space complexity: O(n*len(denom)), since the memo is a (n+1)*len(denom) matrix.
    '''
    @staticmethod
    def numWaysMakeChangeRecMemo(n, denoms):
        
        def helper(n, denoms, d, memo):
            print("n={}, d={}".format(n,d))
            print("memo:")
            for row in memo:
                print("\t",row)
            
            if n < 0:
                return 0
            if n == 0:
                return 1
            if d < 0:
                return 0
            
            if memo[n][d] != None:
                print("found memo: ", memo[n][d])
                return memo[n][d]
            
            nwWithDenom = helper(n-denoms[d], denoms, d, memo)
            nwWithoutDenom = helper(n, denoms, d-1, memo)
            memo[n][d] = nwWithDenom + nwWithoutDenom
            
            return memo[n][d]
        
        # init memo
        memo = [[None for _ in range(len(denoms))] for _ in range(n+1)]
        return helper(n, denoms, len(denoms)-1, memo)
    
    '''
    Time complexity: O(len(denoms)^n), since for each helper call, there are len(denom) helper calls.
    Space complexity: O(n), there are at most n items on the recursive call stack.
    '''
    @staticmethod
    def numWaysMakeChangeRec2(n, denoms):
        
        def helper(n, denoms, d):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            nw = 0
            for i in range(d+1):
                nw += helper(n-denoms[i], denoms, i)
                
            return nw
        
        return helper(n, denoms, len(denoms)-1)
    
    '''
    Time complexity: O(n)
    Space complexity: O(n*len(denoms))
    '''
    @staticmethod
    def numWaysMakeChangeRec2Memo(n, denoms):
        def helper(n, denoms, d, memo):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            if memo[n][d] != None:
                print("memo found: ", memo[n][d])
                return memo[n][d]
            
            nw = 0
            for i in range(d+1):
                nw += helper(n-denoms[i], denoms, i, memo)
            memo[n][d] = nw
            
            return memo[n][d]
        
        memo = [[None for _ in range(len(denoms))] for _ in range(n+1)]
        return helper(n, denoms, len(denoms)-1, memo)  

    """
    Complexity
    Time: O(n*len(denoms)), because you need for loop for denoms, and for loop for n
    Space: O(n), because you need an array to store up to n values.
    """
    @staticmethod
    def numWaysMakeChangeDP(n, denoms):
        denoms = sorted(denoms)
        
        # init array to keep track of ways to make change up to n
        waysForAmt = [0] * (n+1)
        waysForAmt[0] = 1 # because for n=0, there is only 1 way to make change, and that is with no coins.
        #print("waysForAmt: ", waysForAmt)
        
        for d in range(len(denoms)):
            for i in range(n+1):
                denom = denoms[d]
                print("denom: {}, i: {}".format(denom, i))
                if i >= denom:
                    waysForAmt[i] += waysForAmt[i-denom]
            print("waysForAmt: ", waysForAmt)
        
        # the last value will result in the total num of ways to make change
        return waysForAmt[-1]
        
    @staticmethod
    def test1(alg):
        n = 6
        denoms = [1,5]
        alg(n, denoms)
    
    @staticmethod
    def test2(alg):
        n = 9
        denoms = [5,1]
        alg(n, denoms)
    
    @staticmethod
    def test3(alg):
        n = 25
        denoms = [1,5,10,25] # correct ans: 13
        
        #n = 6
        #denoms = [1,5]
        ways = alg(n, denoms)
        print("test3: ways: ", ways)
    
    @staticmethod
    def test4(alg):
        n = 0
        denoms = [1,2,3,4]
        ways = alg(n, denoms)
        print("test4: ways: ", ways)

#alg = Prob.numWaysMakeChangeRec
#alg = Prob.numWaysMakeChangeRecMemo
#alg = Prob.numWaysMakeChangeRec2
#alg = Prob.numWaysMakeChangeRec2Memo
alg = Prob.numWaysMakeChangeDP

#Prob.test1(alg)
#Prob.test2(alg)
Prob.test3(alg)
#Prob.test4(alg)