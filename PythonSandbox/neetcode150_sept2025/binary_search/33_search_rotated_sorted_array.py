from typing import List, Callable

class SearchRotatedSortedArray:
    """
    Time complexity: O(log n) - binary search to find min val index, another binary search to find target
    Space complexity: O(1) - only single value variables used
    """
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        minValIdx = lo
        # print("minValIdx: ", minValIdx)

        if minValIdx == 0:
            lo, hi = 0, len(nums)-1
        elif nums[0] <= target <= nums[minValIdx-1]:
            lo, hi = 0, minValIdx - 1
        else:
            lo, hi = minValIdx, len(nums)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1

        return -1



    def test1(self):
        FN_TO_TEST: Callable = self.search

        tests = [
            dict(nums=[4,5,6,7,0,1,2], target=0, expected=4),
            dict(nums=[4,5,6,7,0,1,2], target=3, expected=-1),
            dict(nums=[1], target=0, expected=-1),
            dict(nums=[3, 1], target=3, expected=0),
            dict(nums=[1], target=1, expected=0),
            dict(nums=[1,3], target=3, expected=1),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i} \nCASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["nums"], tc["target"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation

if __name__ == "__main__":
    c = SearchRotatedSortedArray()
    c.test1()
