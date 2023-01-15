'''
https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        prods = [1]
        for i in range(0, len(nums)-1):
            prods.append(prods[-1]*nums[i])
        #print("prods: ", prods)                
        
        latestProdFromLeft = 1
        for i in range(len(nums)-1, -1, -1):
            prods[i] = prods[i] * latestProdFromLeft
            latestProdFromLeft = latestProdFromLeft*nums[i]
        
        return prods