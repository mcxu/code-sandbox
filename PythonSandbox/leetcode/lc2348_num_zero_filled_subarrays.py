"""
Number of Zero-Filled Subarrays
https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroSubarrays = [0] * len(nums)

        numSubarraysSoFar = 0
        for i,n in enumerate(nums):
            if nums[i] == 0:
                zeroSubarrays[i] = zeroSubarrays[i-1] + 1
                numSubarraysSoFar += zeroSubarrays[i]
        
        return numSubarraysSoFar
