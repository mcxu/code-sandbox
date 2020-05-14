'''
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an array of integers nums and a positive integer k, find whether it's possible to 
divide this array into k non-empty subsets whose sums are all equal.

https://medium.com/@null00/leetcode-partition-to-k-equal-sum-subsets-b08841f3e578
'''
class Solution:
    def canPartitionKSubsets(self, nums, k):
        numsSum = sum(nums)
        print("numsSum: ", numsSum)
        # can divide into k subsets of equal sum
        if numsSum % k == 0:
            targetSum = numsSum/k 
            print("targetSum: ", targetSum)
            #chosenInds = [0 for _ in range(len(nums))] # keep track of indices of chosen values for a subset
            chosenInds = []
            overallResult = True
            for i in range(k):
                print("---- k=", i)
                print("chosenInds before: ", chosenInds)
                [res, chosenInds] = self.helper(nums, len(nums)-1, targetSum, chosenInds)
                print("res: ", res)
                print("chosenInds after: ", chosenInds)
                overallResult = overallResult & res
            return overallResult
        return False
        
        
    def helper(self, nums, i, targetSum, chosenInds):
        print("    helper: i={}, chosenInds: {}".format(i, chosenInds))
        if targetSum < 0:
            print("A")
            return [False, chosenInds]
        if targetSum == 0:
            print("B")
            return [True, chosenInds]
        if i < 0:
            print("C")
            return [False, chosenInds]
        if i == 0:
            print("D")
            if targetSum == 0:
                print("E")
                return [True, chosenInds]

        if i in chosenInds:
            print("    i={} already in chosenInds".format(i))
            return self.helper(nums, i-1, targetSum, chosenInds)
        else:
            excludeRes = self.helper(nums, i-1, targetSum, chosenInds)
            includeRes = self.helper(nums, i-1, targetSum-nums[i], chosenInds+[i])
            result = excludeRes[0]|includeRes[0]
            return [result, includeRes[1] if result == True else excludeRes[1]]
        
    def test1(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        # Output: True
        # Explanation: It's possible to divide it into 4 subsets 
        # (5), (1, 4), (2,3), (2,3) with equal sums.
        res = self.canPartitionKSubsets(nums, k)
        print("test1 res: ", res)
        
    def test2(self):
        nums = [2,2,2,2,3,4,5]; k = 4 # Expected: False
        #nums = [2,3,4,5]; k = 4
        res = self.canPartitionKSubsets(nums, k)
        print("test2 res: ", res)

    def test3(self):
        nums = [1,1,1,1,1,1,1,1,1,1]
        k = 5
        res = self.canPartitionKSubsets(nums, k)
        print("test3 res: ", res)

s = Solution()
s.test1()
#s.test2()
#s.test3()
