'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            m = int((lo+hi)/2)
            #print("lo: {}, hi: {} m:{} ".format(lo,hi,m))
            if m-1>=0 and nums[m] < nums[m-1]:
                return nums[m]
            
            if nums[lo] <= nums[m] and nums[m] > nums[hi]:
                lo = m+1
            else:
                hi = m-1
        
        return nums[lo]