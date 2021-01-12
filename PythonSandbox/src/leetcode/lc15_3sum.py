'''
https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import unittest

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        triplets = set()
        for i,n in enumerate(nums):
            neg = -1*n
            pairsFromi = self.twoSum(nums, i+1, neg)
            for p in pairsFromi:
                newtriplet = tuple(sorted([n, p[0], p[1]]))
                if newtriplet not in triplets:
                    triplets.add(newtriplet)
        return triplets
    
    def twoSum(self, num, i, target):
        visited = set()
        pairs = set()
        for j in range(i, len(num)):
            val = num[j]
            if target-val in visited:
                newpair = (target-val, val)
                if newpair not in pairs:
                    pairs.add(newpair)
            else:
                visited.add(val)
        
        return pairs

# TLE
class Solution2:
    def threeSum(self, nums: [int]) -> [[int]]:
        target = 0
        nums = sorted(nums)
        triplets = set()
        for i in range(len(nums)-2):
            self.helper(nums, target, i, i+1, len(nums)-1, triplets)
        return triplets
        
    def helper(self, nums, target, a, b, c, triplets):
        if b >= c:
            return
        
        aval=nums[a]; bval=nums[b]; cval=nums[c]
        currTriplet = (aval, bval, cval)
        currSum = sum(currTriplet)
        
        if currSum==target and currTriplet not in triplets:
            triplets.add(currTriplet)
        
        if currSum < target:
            self.helper(nums, target, a, b+1, c, triplets)
        else:
            self.helper(nums, target, a, b, c-1, triplets)


class Test(unittest.TestCase):

    def test_threeSum1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        sol = Solution()
        result = sol.threeSum(nums)
        print("result: ", result)
        for t in expected:
            self.assertIn(t, result)

    # def test_threeSum2(self):
    #     nums = [-2,0,1,1,2]
    #     expected = [[-2,0,2],[-2,1,1]]
    #     sol = Solution()
    #     result = sol.threeSum(nums)
    #     print("result: ", result)
    #     for t in expected:
    #         self.assertIn(t, result)

unittest.main()