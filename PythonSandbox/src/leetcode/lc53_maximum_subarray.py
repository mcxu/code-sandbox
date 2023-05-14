"""
https://leetcode.com/problems/maximum-subarray/
(Kadane's Algorithm)
"""
class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def maxSubArray(self, nums:[int]) -> int:
        maxSumSoFar = -float('inf')
        maxSumUpToN = 0

        for i,n in enumerate(nums):

            if maxSumUpToN + n > n:
                maxSumUpToN = maxSumUpToN + n
            else:
                maxSumUpToN = n
            
            maxSumSoFar = max(maxSumSoFar, maxSumUpToN)
        
        return maxSumSoFar
            
    def maxSubArray_getSubarray(self, nums):
        maxSumSoFar = -float('inf')
        maxSumUpToN = 0

        startIdx = 0
        endIdx = 0
        for i,n in enumerate(nums):
            if maxSumUpToN + n > n:
                maxSumUpToN = maxSumUpToN + n
            else:
                maxSumUpToN = n
                startIdx = i
            
            if maxSumUpToN > maxSumSoFar:
                maxSumSoFar = maxSumUpToN
                endIdx = i
        
        return maxSumSoFar, [startIdx, endIdx]
    
    def test_maxSubArray_getSubarray(self):
        a = [-2,1,-3,4,-1,2,1,-5,4] # expected: [4 -1 2 1]
        res = self.maxSubArray_getSubarray(a)
        print("res: ", res)
        indices = res[1]
        startIdx, endIdx = indices[0], indices[1]
        
        subArray = a[startIdx: endIdx+1]
        print("The actual subarray: ", subArray)
        print("The sum: ", sum(subArray))

    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def maxSubArray2(self, nums: [int]) -> int:
        maxSumUpTo = [0 for _ in range(len(nums))]
        maxSumUpTo[0] = nums[0]
        
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            maxSumUpTo[i] = max(n, maxSumUpTo[i-1]+n)
            
            if maxSumUpTo[i] > maxSoFar:
                maxSoFar = maxSumUpTo[i]
        return maxSoFar

s = Solution()
s.test_maxSubArray_getSubarray()