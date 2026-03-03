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

class Solution2:
    def threeSum(self, nums: [int]) -> [[int]]:
        triplets = set()
        for i,n in enumerate(nums):
            target = -n # find twoSum that add up to opposite of n
            pairsFromIdx = self.twoSumFromIdx(i+1, nums, target) # get pairs from i+1 (twoSum)

            for tup in pairsFromIdx:
                newTriplet = tuple(sorted([n, tup[0], tup[1]]))
                if newTriplet not in triplets:
                    triplets.add(newTriplet)
        return triplets


    def twoSumFromIdx(self, j, nums, target):
        validPairs = set()
        seenNums = set()
        for k in range(j, len(nums)):
            if target - nums[k] in seenNums:
                validPairs.add((nums[k], target-nums[k]))
            else:
                seenNums.add(nums[k])
        return validPairs

    def test(self):
        cases = [
            dict(nums=[-1,0,1,2,-1,-4], output=[[-1,-1,2],[-1,0,1]]),
            dict(nums=[0,1,1], output=[]),
            dict(nums=[0,0,0], output=[[0,0,0]])
        ]

        for c in cases:
            res = self.threeSum(c["nums"])
            print("case: ", c["nums"])
            print("res: ", res)
            assert res == c["output"]



sol2 = Solution2()
sol2.test()


# TLE ===========================================================
class Solution:
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
        sol = Solution2()
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

#unittest.main()