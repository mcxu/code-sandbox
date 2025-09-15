'''
https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and uses constant extra space.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
'''

class Solution:
    # Not constant extra space, but Accepted.
    def firstMissingPositive(self, nums: [int]) -> int:
        if not nums:
            return 1

        minNum = min(nums)
        maxNum = max(nums)

        if minNum > 1 and maxNum >= minNum:
            return 1

        if minNum <= 0:
            minNum = 1
        
        numSet = set(nums)
        i = minNum
        while i < maxNum+1:
            if i not in numSet:
                return i
            i += 1
        return i
    
    def test1(self):
        #input = [1,2,0]
        #input = [3,4,-1,1]
        #input = [7,8,9,11,12]
        res = self.firstMissingPositive(input)
        print("test1 res: ", res)

    def test2(self):
        #input = [2] # expected: 1
        #input = [-2]
        input = [2,1]
        res = self.firstMissingPositive(input)
        print("test2 res: ", res)

s = Solution()
#s.test1()
s.test2()