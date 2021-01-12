# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: [int]) -> bool:
        lowestStartPosition = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= lowestStartPosition:
                lowestStartPosition = i
        
        return lowestStartPosition == 0