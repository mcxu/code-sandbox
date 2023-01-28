'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
'''
class Solution:
    def findMin(self, nums: [int]) -> int:
        i = 0
        j = len(nums)-1

        while i <= j:
            midIdx = (i+j)//2

            if midIdx-1 >= 0 and nums[midIdx-1] > nums[midIdx]:
                return nums[midIdx]
            
            if nums[i] <= nums[midIdx] and nums[midIdx] > nums[j]:
                i = midIdx + 1
            else:
                j = midIdx - 1
        
        return nums[i]
    
