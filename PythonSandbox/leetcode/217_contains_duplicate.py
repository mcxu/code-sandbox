"""
https://leetcode.com/problems/contains-duplicate/description/

Time complexity: O(n), where n ~ len(nums)
Space complexity: O(n), where n ~ len(nums)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()
        for i,n in enumerate(nums):
            if n in seenNums:
                return True
            else:
                seenNums.add(n)
        return False