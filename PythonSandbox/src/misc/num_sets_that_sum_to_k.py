'''
Given array and a target number k, find number of subsets that sum up to k

Example:
arr = [2,4,6,10]
k = 16
'''

class Prob:
    '''
    Recursive brute force.
    Let n = len(arr)
    Time complexity: O(2^n), since each call of helper produces 2 recursive calls of helper.
    Space complexity: O(n), since there are at most n helper calls on the call stack.
    '''
    @staticmethod
    def numSubsets(arr, k):
        
        def helper(arr, remainder, i):
            nonlocal c
            if remainder == 0:
                return 1
            if remainder < 0:
                return 0
            if i < 0:
                return 0 # since i<0 means a number not even on the array.
            
            currValue = arr[i] # current value
            
            # if you've excluded currvalue as part of a valid subset, 
            # then you don't substract this value from remainder.
            excludeCurrValue = helper(arr, remainder, i-1)
            
            # if you've included currvalue as part of a valid subset,
            # then you can't include currvalue again next time, so substract it from remainder. 
            includeCurrValue = helper(arr, remainder-currValue, i-1)
            c += 1
            return excludeCurrValue + includeCurrValue
        
        c = 0
        ns = helper(arr, k, len(arr)-1)
        print("c: ", c)
        return ns 
    
    '''
    Recursive memoized; memoize each 'node' of calls in the tree:
    memo = (subproblem where curr value is excluded) + (subproblem where curr value is included)
    Let n = 
    '''
    @staticmethod
    def numSubsetsMemo(arr, k):
        
        def helperMemo(arr, remainder, i, memo):
            nonlocal c
            print("memo: ", memo)
            if remainder == 0:
                return 1
            if remainder < 0:
                return 0
            if i < 0:
                return 0
            
            if remainder in memo.keys():
                return memo[remainder]
            
            excludeCurrValue = helperMemo(arr, remainder, i-1, memo)
            includeCurrValue = helperMemo(arr, remainder-arr[i], i-1, memo)
            memo[remainder] = excludeCurrValue + includeCurrValue
            c += 1
            return memo[remainder]
        
        c = 0 
        memo = {}
        ns = helperMemo(arr, k, len(arr)-1, memo)
        print("c: ", c)
        return ns
    
    @staticmethod
    def test1(alg):
        arr = [2,4,6,10,12]
        k = 16
        res = alg(arr, k)
        print("test1 res: ", res)

alg = Prob.numSubsets
#alg = Prob.numSubsetsMemo
Prob.test1(alg)
