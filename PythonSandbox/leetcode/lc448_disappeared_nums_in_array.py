'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [5,6]
'''
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        numsSet = set(nums)
        out = []
        for i in range(1, len(nums)+1):
            if i not in numsSet:
                out.append(i)
        return out
    
    def test1(self):
        input = [4,3,2,7,8,2,3,1]
        res = self.findDisappearedNumbers(input)
        print("test1 res: ", res)

s = Solution()
s.test1()