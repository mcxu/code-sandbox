# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for n in nums:
            for i in range(len(powerset)):
                newset = powerset[i] + [n]
                powerset.append(newset)
        return powerset