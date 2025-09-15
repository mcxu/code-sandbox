'''
136. Single Number
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.
Note: Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = set([]) # memo
        for i in range(len(nums)):
            n = nums[i]
            if n in m:
                m.remove(n)
            else:
                m.add(n)
        return list(m)[0]