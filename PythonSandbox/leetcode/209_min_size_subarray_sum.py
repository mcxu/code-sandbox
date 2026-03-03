# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        subarrayLen = float('inf')
        runSum = 0 
        loIdx = 0
        for i,n in enumerate(nums):
            runSum += n

            while runSum >= target:
                subarrayLen = min(subarrayLen, i-loIdx+1)
                runSum -= nums[loIdx]
                loIdx += 1

        return subarrayLen if subarrayLen != float('inf') else 0
    
    '''
    Time complexity: O(n) where n ~ len(nums)
    Space complexity: O(1), since we aren't using any data structures that expand with nums
    '''
    def minSubArrayLen2(self, target: int, nums: [int]) -> int:
        subarrayLen = float('inf')
        runSum = 0 
        loIdx = 0
        i = 0
        while i < len(nums):
            if runSum >= target:
                if loIdx < len(nums) and loIdx < i:
                    subarrayLen = min(subarrayLen, i - loIdx)
                    runSum -= nums[loIdx]
                    loIdx += 1
            else:
                runSum += nums[i]
                i += 1

        while loIdx < len(nums):
            if runSum >= target:
                subarrayLen = min(subarrayLen, i - loIdx)
                runSum -= nums[loIdx]
                
            loIdx += 1    

        return subarrayLen if subarrayLen != float('inf') else 0
        
    def test(self):
        cases = [
            #dict(target=7, nums=[2,3,1,2,4,3], expected=2),
            #dict(target=4, nums=[1,4,4], expected=1),
            #dict(target=11, nums=[1,1,1,1,1,1,1,1], expected=0)
            dict(target=11, nums=[1,2,3,4,5], expected=3)
        ]

        for c in cases:
            print("executing case: ", c)
            result = self.minSubArrayLen(c["target"], c["nums"])
            print("result: ", result)
            assert result == c["expected"]

