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
    

    def test1(self):
        nums = [3,4,5,1,2]
        result = self.findMin(nums)
        print("result: ", result)
        actual = 1
        assert result == actual, "Test failed"
        

if __name__ == "__main__":
    sol = MinInRotatedSortedArray()
    sol.test1()