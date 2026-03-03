"""
https://leetcode.com/problems/global-and-local-inversions/description/
"""
from typing import List

class Solution:
    """ Notes: This solution results in TLE
    Time complexity: O(n*logn) from the merge sort
    Space complexity: O(1), no auxiliary data structures other than nums which doesn't count
    """
    def isIdealPermutation(self, nums: List[int]) -> bool:
        localCount = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                localCount += 1

        _, globalCount = self.mergeSortAndCount(nums)
        return globalCount == localCount

    def mergeSortAndCount(self, nums):
        if len(nums) <= 1:
            return nums, 0 # nums, global
        
        ltSubarray, ltGlobal = self.mergeSortAndCount(nums[:len(nums)//2])
        rtSubarray, rtGlobal = self.mergeSortAndCount(nums[len(nums)//2:])

        globalCount = ltGlobal + rtGlobal
        mergedArr = []

        i, j = 0,0
        while i < len(ltSubarray) and j < len(rtSubarray):
            if ltSubarray[i] <= rtSubarray[j]:
                mergedArr.append(ltSubarray[i])
                i += 1
            else:
                mergedArr.append(rtSubarray[j])
                globalCount += len(ltSubarray)-i
                #print(f"i:{i}, j:{j}, added {len(ltSubarray)-i} to globalCount: {globalCount}")
                j += 1

        mergedArr += ltSubarray[i:]
        mergedArr += rtSubarray[j:]
        
        return mergedArr, globalCount

    def test(self):
        #nums = [1,0,2] # expected True: There is 1 global inversion and 1 local inversion.
        nums = [1,2,0] # expected False: There are 2 global inversions and 1 local inversion.
        result = self.isIdealPermutation(nums)
        print("result: ", result)

s = Solution()
s.test()