'''
213. House Robber II
https://leetcode.com/problems/house-robber-ii/
Each house has a certain amount of money stashed. ALL HOUSES ARE ARRANGED IN A CIRCLE. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were 
broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob0 = self.helper(nums, 0, True, {})
        notrob0 = self.helper(nums, 1, False, {})
        return max(rob0, notrob0)
    
    def helper(self, nums, i, robbed0th, memo):
        if len(nums)==1:
            return nums[0]
            
        if robbed0th == True and i == len(nums)-1:
            return 0
        if i > len(nums)-1:
            return 0
        
        if i in memo.keys():
            return memo[i]
        
        jump1 = self.helper(nums, i+1, robbed0th, memo)
        jump2 = self.helper(nums, i+2, robbed0th, memo) + nums[i]
        memo[i] = max(jump1, jump2)
        return memo[i]