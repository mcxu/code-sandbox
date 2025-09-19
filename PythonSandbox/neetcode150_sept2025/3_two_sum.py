from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # num -> index
        for idx,n in enumerate(nums):
            diff = target-n
            if diff in numMap:
                secondIdx = numMap[diff]
                return [idx, secondIdx]
            else:
                numMap[n] = idx
        return [None, None]