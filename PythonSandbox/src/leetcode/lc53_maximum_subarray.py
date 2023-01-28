class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxSumSoFar = nums[0]
        maxSumUpTo = nums[0]

        for i in range(1, len(nums)):
            if maxSumUpTo + nums[i] > nums[i]:
                maxSumUpTo = maxSumUpTo + nums[i]
            else:
                maxSumUpTo = nums[i]

            if maxSumUpTo > maxSumSoFar:
                maxSumSoFar = maxSumUpTo
        
        return maxSumSoFar
            

    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def maxSubArray2(self, nums: List[int]) -> int:
        maxSumUpTo = [0 for _ in range(len(nums))]
        maxSumUpTo[0] = nums[0]
        
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            maxSumUpTo[i] = max(n, maxSumUpTo[i-1]+n)
            
            if maxSumUpTo[i] > maxSoFar:
                maxSoFar = maxSumUpTo[i]
        return maxSoFar