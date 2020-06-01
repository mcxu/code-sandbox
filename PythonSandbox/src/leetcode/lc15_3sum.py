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
    def threeSum(self, nums):
        triplets = set([])

        for i in range(len(nums)-1):
            twoSumTarget = -1*nums[i]
            twoSumResult = self.twoSum(nums, i+1, twoSumTarget)
            for result in twoSumResult:
                t = sorted([nums[i], result[0], result[1]])
                tTup = tuple(t)
                if tTup not in triplets:
                    triplets.add(tTup)
        return [list(trip) for trip in triplets]
    
    def twoSum(self, nums, i, target):
        aux = set([])
        out = set([])
        for j in range(i, len(nums)):
            if target - nums[j] in aux:
                out.add((nums[j], target-nums[j]))
            else:
                aux.add(nums[j])
        return out


    # def threeSum(self, nums):
    #     nums = sorted(nums)
    #     if len(nums) >= 3 and nums[0]==0 and nums[0]==nums[-1]:
    #         return [[0,0,0]]
        
    #     triplets = set([])

    #     for i in range(len(nums)-2):
    #         self.tripletHelper(i, i+1, len(nums)-1, nums, triplets)
        
    #     return [list(triplet) for triplet in triplets]
    
    # def tripletHelper(self, i, j, k, nums, triplets):
    #     if j >= k:
    #         return
        
    #     currTriplet = (nums[i], nums[j], nums[k])
    #     ctSum = sum(currTriplet)

    #     if ctSum == 0 and currTriplet not in triplets:
    #         triplets.add(currTriplet)

    #     if ctSum > 0:
    #         self.tripletHelper(i, j, k-1, nums, triplets)
    #     else:
    #         self.tripletHelper(i, j+1, k, nums, triplets)


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