"""
Given a collection of distinct integers, return all possible permutations. [Medium]
Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

#import time
import sys
from utils.number_utils import NumberUtils
sys.setrecursionlimit(10**6)

class LC46:
    # number of permutations in entire list
    def permute(self, nums):
        # helper function
        def permuteHelper(nums, results):
            if nums in results:
                #print("    list {} already in results.".format(nums))
                return results
            else:
                #print("    appending {} to results.".format(nums))
                results.append(nums)
            #print("results: ", results)
            
            for i in range(len(nums)-1):
                #print("    i:{}, nums:{}".format(i,nums))
                newPerm = nums.copy()
                # swap the ith and (i+1)th, to make a new permutation
                tmp = newPerm[i+1]
                newPerm[i+1] = newPerm[i]
                newPerm[i] = tmp
                #print("    after swap: nums:{}, newPerm:{}".format(nums, newPerm))
                
                # recursive call
                permuteHelper(newPerm, results)
                
            return results
        
        # populate list of results using permuteHelper
        return permuteHelper(nums, [])
            
    def test_permute(self):
        numsList = [
            [1,2,3],
            [1,2,3,4],
            [1,2,3,4,5,6]]
        
        for nums in numsList:
            results = self.permute(nums)
            print("test_permute nums: ", nums)
            print("test_permute results: ", results)
            print("test_permute number of permutations: ", len(results))
            print("")
    
    # find all k-permutations from a list of n-elements
    # by filtering out all [0:k] duplicates from permuting entire list
    def test_permute_partial(self):
        numsList = [
            [1,2,3],
            [1,2,3,4],
            [1,2,3,4,5,6]]
        k = 2
        for nums in numsList:
            #k = len(nums) # same as permuting entire list
            results = self.permute(nums)
            resultsCopy = results.copy()
            results_k = []
            for i in range(len(results)):
                results[i] = results[i][:k]
                if results[i] not in results_k:
                    results_k.append(results[i])
                
            print("test_permute_partial nums: ", nums)
            print("test_permute_partial results: ", resultsCopy)
            print("test_permute_partial results_k: ", results_k)
            print("test_permute_partial number of permutations: ", len(results))
            print("test_permute_partial number of k-permutations: ", len(results_k))
            print("")
    
    # n items taken k at a time (order matters)
    def nPk_formula(self, n, k):
        perms = NumberUtils.factorial(n)/NumberUtils.factorial(n-k)
        return int(perms)
    
    def test_nPk_formula(self):
        n = 6
        k = 1
        ans = self.nPk_formula(n, k)
        print("num permutations: ", ans)
     
def main():
    lc46 = LC46()
    #lc46.test_permute()
    lc46.test_permute_partial()
    #lc46.test_nPk_formula()

main()
            
        