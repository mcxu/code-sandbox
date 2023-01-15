# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        minSize = float('inf')
        runSum = 0
        i = 0 # left pointer
        for j,n in enumerate(nums): # right pointer
            runSum += n
            
            while runSum >= s:
                minSize = min(minSize, j-i+1)
                runSum -= nums[i]
                i += 1
                
        return minSize if minSize != float('inf') else 0