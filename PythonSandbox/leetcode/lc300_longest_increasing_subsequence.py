class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longestUpToVal = [1 for _ in nums]
        longestSoFar = 1
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and longestUpToVal[j]+1 > longestUpToVal[i]:
                    longestUpToVal[i] = longestUpToVal[j]+1
                
                longestSoFar = max(longestSoFar, longestUpToVal[i])
        
        #print("longestUpToVal: ", longestUpToVal)

        return longestSoFar