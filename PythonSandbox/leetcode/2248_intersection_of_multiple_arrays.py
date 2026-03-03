# https://leetcode.com/problems/intersection-of-multiple-arrays/description/

from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numSet = set(nums[0])
        
        for i in range(1, len(nums)):
            innerArr = nums[i]
            numSet = numSet.intersection(set(innerArr))
            
        return sorted(numSet)

                