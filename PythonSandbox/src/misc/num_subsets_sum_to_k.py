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
    Space complexity: O(n), since there are at most n helper calls on the call stack (the depth of the recursion tree)
    '''
    @staticmethod
    def numSubsets(arr, k):
        
        def helper(arr, remainder, i):
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
            
            return excludeCurrValue + includeCurrValue
        
        ns = helper(arr, k, len(arr)-1)
        return ns 
    
    @staticmethod
    def test1(alg):
        #arr = [2,4,6,10,12]
        arr = [2,4,6,12,10]
        k = 16
        res = alg(arr, k)
        print("test1 res: ", res)

alg = Prob.numSubsets
Prob.test1(alg)
