'''
198. House Robber
https://leetcode.com/problems/house-robber/
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        startFrom0 = self.helper(nums, 0, {}) # start from 0th index
        return startFrom0
    
    
    def helper(self, nums, i, memo):
        #print("i = ", i)
        if len(nums) == 2:
            return max(nums)
        
        if i > len(nums)-1:
            return 0
        
        if i in memo.keys():
            return memo[i]
        
        jump1FromCurr = self.helper(nums, i+1, memo)
        jump2FromCurr = self.helper(nums, i+2, memo) + nums[i]
        memo[i] = max(jump1FromCurr, jump2FromCurr)
        return memo[i]
        #return max(jump1FromCurr, jump2FromCurr)