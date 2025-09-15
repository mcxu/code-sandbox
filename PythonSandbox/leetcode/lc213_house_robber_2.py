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
    def rob(self, nums: [int]) -> int:
        rewardRob0 = self.jump(nums, 0, True, {})
        rewardNotRob0 = self.jump(nums, 1, False, {})
        maxReward = max(rewardRob0, rewardNotRob0)
        return maxReward
    
    def jump(self, nums, i, robbed0thHouse, memo):
        if len(nums) == 1:
            return nums[0]

        if i >= len(nums):
            return 0

        if robbed0thHouse and i == len(nums)-1:
            return 0

        if i in memo.keys():
            return memo[i]

        dontRobCurrent = self.jump(nums, i+1, robbed0thHouse, memo)
        robCurrent = self.jump(nums, i+2, robbed0thHouse, memo) + nums[i]
        maxReward = max(dontRobCurrent, robCurrent)
        memo[i] = maxReward
        return maxReward