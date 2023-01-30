"""
https://leetcode.com/problems/combination-sum-iv/description/
"""

class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        memo = {}
        return self.buildSolution(nums, target, memo)
    
    def buildSolution(self, nums, target, memo):

        if target < 0:
            return 0

        if target == 0:
            return 1

        if target in memo.keys():
            return memo[target]

        numCombos = 0
        for i in range(len(nums)):
            n = nums[i]
            numCombos += self.buildSolution(nums, target-n, memo)
        
        memo[target] = numCombos
        return numCombos

    def test(self):
        cases = [
            # dict(candidates=[1,2,3], target=4, expected=7),
            dict(candidates=[4,2,1], target=32, expected=39882198)
        ]

        for case in cases:
            print("case: ", case)
            res = self.combinationSum4(case["candidates"], case["target"])
            print("res: ", res)
            assert res == case["expected"]

sol = Solution()
sol.test()