# https://leetcode.com/problems/find-peak-element/

class Solution:
    # O(logn) time using binary search
    def findPeakElement2(self, nums: [int]) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            m = int((i+j)/2)
            
            if m+1 < len(nums) and nums[m] < nums[m+1]:
                i = m + 1
            else:
                j = m - 1
        
        return i


    # O(n) time
    def findPeakElement1(self, nums: [int]) -> int:
        if len(nums)==1:
            return 0
        
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        
        if nums[0] > nums[1]:
            return 0
        elif nums[-2] < nums[-1]:
            return len(nums)-1

        return 0