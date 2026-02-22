from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for i in range(len(nums)):
            for j in range(len(powerset)):
                subset = powerset[j] + [nums[i]]
                powerset.append(subset)
        # print("powerset: ", powerset)
        return powerset
    
    def test1(self):
        nums = [1,2,3]
        result = self.subsets(nums)
        print("result: ", result)

if __name__ == "__main__":
    s = Solution()
    s.test1()