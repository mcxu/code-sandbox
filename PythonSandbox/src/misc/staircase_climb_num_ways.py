'''
You are at the bottom of a staircase. You can jump 1, 2, or 3 stairs at a time. 
How many different ways can you jump up the stairs?
'''

class Prob:
    '''
    Let n = number of steps.
    Time complexity: O(3^n), since each call produces 3 recursive calls.
    Space complexity: O(d), where d = depth, and d ~ n, since the recursive calls go from n to 0
    '''
    @staticmethod
    def numWaysUpStairsRec(n):
        if n < 0:
            # If the last recursion in a path hits this base case, it means that a path composed of its sequence of jumps cannot get to the 0th step exactly.
            # So this means no paths exists, return 0.
            return 0
        if n == 0:
            # if n==0, then you are already at the only solution. since there is a solution, there is a way, so return 1 (num of ways).
            # another way to think about this. IF you can only jump n stairs as a step, then you will reach this base case upon 
            # entering this function. But that is already 1 way. For example if n=10, but you can only jump 10 stairs as a step 
            #(you have very long legs), then that is 1 way, so return 1.
            return 1 
        
        numWays = Prob.numWaysUpStairsRec(n-1) + \
            Prob.numWaysUpStairsRec(n-2) + \
            Prob.numWaysUpStairsRec(n-3)
        return numWays
    
    @staticmethod
    def test1():
        n = 4
        #n = 10
        numWays = Prob.numWaysUpStairsRec(n)
        print("test1 numWays: ", numWays)
    
    '''
    With memoization to save the results of previous subproblems.
    Let n = number of stairs
    Time complexity: O(n), since the 3 calls for each value of n get stored in a map, and lookup time in map is O(1).
    Space complexity: O(n), since each call from n-0 gets put on the map.
    '''
    @staticmethod
    def numWaysUpStairsRecMemo(n):
        def helper(n, memo):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            #print("memo.keys:", memo.keys())
            if n not in memo.keys():
                numWays = helper(n-1, memo) + helper(n-2, memo) + helper(n-3, memo)
                memo[n] = numWays
            
            return memo[n]
        
        memo = {}
        return helper(n, memo)

    @staticmethod
    def test2():
        #n = 4
        n = 10
        numWays = Prob.numWaysUpStairsRecMemo(n)
        print("test2 numWays: ", numWays)
    
    '''
    Dynamic programming.
    Let n = num stairs
    Time complexity: O(n), since there is a single forloop that iterates from [2,n+1] which is O(n) time.
    Space complexity: O(n), since numWays stores at most n solutions.
    '''
    @staticmethod
    def numWaysUpStairsDP(n):
        '''
        0 stairs: 1 ways possible (look at reasoning in brute force recursive solution)
        1 stair: 1 way possible 
        '''
        numWays = [0 for _ in range(n+1)]
        if n >= 0:
            numWays[0] = 1
        if n >= 1:
            numWays[1] = 1
        
        print("numWays init: ", numWays)
        for i in range(2, n+1):
            numWays[i] = numWays[i-1]+numWays[i-2]+numWays[i-3]
        print("numWays: ", numWays)
        return numWays[n]
        
    @staticmethod
    def test3():
        #n = 0
        #n = 4
        n = 10
        numWays = Prob.numWaysUpStairsDP(n)
        print("test3 numWays: ", numWays)
    
    '''
    Only jumps of specific number of steps allowed.
    Let n=num steps
    Time complexity: For some value of n, there are O(a=len(allowed)) iterations at most, 
        followed by a recursive call of at most n subsequent calls (when a=1) using the map. 
        Therefore, time: O(a*n). If there was no means of memoization, then time: O(a*(2^n))
    Space complexity: O(n), since numWays map stores at most n solutions to subproblems.
    '''
    @staticmethod
    def numWaysUpStairsAllowed(n, allowed):
        def helper(n, memo):
            nonlocal allowed
            if n<0:
                print("below zero recursion found: ", n)
                return 0
            if n==0:
                return 1
            
            if n not in memo.keys():
                numWays = 0
                for a in allowed:
                    print("a: {}, n: {}".format(a,n))
                    numWays += helper(n-a, memo)
                memo[n] = numWays
            
            return memo[n]
        
        memo = {}
        return helper(n, memo)
    
    @staticmethod
    def test4():
        #n = 4 
        #n = 7 # with allowed [1, 5], should return 4
        n = 10
        allowed = [3,2]
        numWays = Prob.numWaysUpStairsAllowed(n, allowed)
        print("test4 numWays: ", numWays)
    
#Prob.test1()
#Prob.test2()
#Prob.test3()
Prob.test4()

