# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: [int], target: int) -> int:
        maxValInd = 0
        for i in range(1, len(nums)):
            curr = nums[i]
            prev = nums[i-1]
            if curr < prev:
                maxValInd = i-1
                break
            elif i == len(nums)-1:
                maxValInd = len(nums)-1
                break
        
        start = 0
        end = len(nums)-1
        if nums[0] <= target <= nums[maxValInd]:
            # binary search between ind 0:maxValInd
            end = maxValInd
        elif maxValInd + 1 <= len(nums)-1 and nums[maxValInd+1] <= target <= nums[-1]:
            # binary search between ind maxValInd:end of array 
            start = maxValInd+1
        
        return self.binSearch(nums, start, end, target)  
        
    def binSearch(self, nums, i, j, target):
        while i <= j:
            m = int((i+j)/2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m+1
            elif nums[m] > target:
                j = m-1
        return -1  