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
        i = 0 # start from 0th index
        memo = {}
        maxReward = self.jump(nums, i, memo)
        return maxReward

    def jump(self, nums, i, memo):
        if i >= len(nums):
            return 0
        
        if i in memo.keys():
            return memo[i]

        dontRobCurrent = self.jump(nums, i+1, memo) # don't include reward of the current house
        robCurrent = self.jump(nums, i+2, memo) + nums[i] # include the reward of the current house
        maxReward = max(dontRobCurrent, robCurrent) # which one leads to the max reward?

        memo[i] = maxReward
        return maxReward