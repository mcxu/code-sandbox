from typing import List

class MinInRotatedSortedArray:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[lo]
