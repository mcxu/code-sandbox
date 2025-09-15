# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lowestIdxThatCanReachEnd = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lowestIdxThatCanReachEnd:
                lowestIdxThatCanReachEnd = i
        return lowestIdxThatCanReachEnd == 0
    
    