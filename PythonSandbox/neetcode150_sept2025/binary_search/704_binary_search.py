from typing import List, Callable

class BS:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = int((lo + hi)/2)
            midNum = nums[mid]

            if target == midNum:
                return mid
            elif target > midNum:
                lo = mid+1
            elif target < midNum:
                hi = mid-1
        
        return -1

    def test1(self):
        FN_TO_TEST: Callable = self.search

        tests = [
            dict(nums=[-1,0,3,5,9,12], target=9, expected=4),
            dict(nums=[-1,0,3,5,9,12], target=2, expected=-1),
            dict(nums=[5], target=5, expected=0)
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["nums"], tc["target"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation

if __name__ == "__main__":
    c = BS()
    c.test1()
