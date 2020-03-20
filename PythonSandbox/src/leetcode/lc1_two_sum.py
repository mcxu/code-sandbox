'''
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        diffMap = {} # diff : index
        for i in range(len(nums)):
            if target - nums[i] in diffMap.keys():
                return [diffMap[target-nums[i]], i]
            else:
                diffMap[nums[i]] = i
        
        return None
        
    
    def test1(self, alg):
        nums = [2, 7, 11, 15]
        target = 9
        indices = alg(nums, target)
        print("indices: ", indices)
    
sol = Solution()
sol.test1(sol.twoSum)