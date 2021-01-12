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
sys.setrecursionlimit(10**6)

class Solution:
    '''
    Let n = number of elmements in list
    Time complexity: O(n!*n). Number of perms formula P(n,r)=n!/(n-r)! so this formula is order n!.
    The extra O(n) comes from the for loop where you are looping from index [0,n-1] elements for each
    current perm to find new perms.
    Space complexity: O(n!*n). Order of n! total perms each corresponding to a helper call on the stack.
    The extra n comes from the for loop, which places n-1 calls on the stack for each current perm.
    '''
    # number of permutations in entire list
    def permute(self, nums):
        c = 0
        # helper function
        def permuteHelper(nums, results):
            nonlocal c
            c += 1
            print("c: ", c)
            if nums in results:
                #print("    list {} already in results.".format(nums))
                return 
            else:
                #print("    appending {} to results.".format(nums))
                numsCopy = nums.copy()
                results.append(numsCopy)
            #print("results: ", results)
            
            for i in range(len(nums)-1):
                # swap the ith and (i+1)th, to make a new permutation
                swap(nums, i, i+1)
                #print("    after swap: nums:{}, newPerm:{}".format(nums, newPerm))
                permuteHelper(nums, results)
                # swap the ith and (i+1)th, to make a new permutation
                swap(nums, i, i+1)
        
        def swap(nums, i, j):
            nums[i],nums[j] = nums[j],nums[i]

        # populate list of results using permuteHelper
        results = []
        permuteHelper(nums, results)
        return results
            
    def test_permute(self):
        numsList = [
            #[1,2,3]
            #[1,2,3,4],
            [1,2,3,4,5,6]
            ]
        
        for nums in numsList:
            results = self.permute(nums)
            print("test_permute nums: ", nums)
            print("test_permute results: ", results)
            print("test_permute number of permutations: ", len(results))
            print("")
    
    # find all permutations of size k in array nums
    def permutePartial(self, nums, k):
        #k = len(nums) # same as permuting entire list
        results = self.permute(nums)
        results_k = []
        for i in range(len(results)):
            results[i] = results[i][:k]
            if results[i] not in results_k:
                results_k.append(results[i])
        return results_k
    
    # find all k-permutations from a list of n-elements
    # by filtering out all [0:k] duplicates from permuting entire list
    def test_permutePartial(self):
        numsList = [
            [1,2,3],
            [1,2,3,4],
            [1,2,3,4,5,6],
            [1,2,3,'a','b','c']]
        k = 3
        for nums in numsList:
            results_k = self.permutePartial(nums, k)
            print("test_permute_partial nums: ", nums)
            print("test_permute_partial results_k: ", results_k)
            print("test_permute_partial number of k-permutations: ", len(results_k))
            print("") 

    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)

    def test_factorial(self):
        n = 4
        res = self.factorial(n)
        print("test_factorial: ", res)

    # n items taken k at a time (order matters)
    def nPk_formula(self, n, k):
        perms = self.factorial(n)/self.factorial(n-k)
        return int(perms)
    
    def test_nPk_formula(self):
        n = 6
        k = 1
        ans = self.nPk_formula(n, k)
        print("num permutations: ", ans)
     
def main():
    s = Solution()
    s.test_permute()
    #s.test_permutePartial()
    #s.test_factorial()
    #s.test_nPk_formula()

main()
            
        