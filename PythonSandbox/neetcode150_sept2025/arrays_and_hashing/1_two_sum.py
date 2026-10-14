from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in idxMap:
                return (i, idxMap[diff])
            else:
                idxMap[n] = i
        return (None, None)