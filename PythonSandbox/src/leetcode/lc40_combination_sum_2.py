'''
40. Combination Sum 2
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

"""
This solution fails due to TLE with this case:
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
"""
import collections
import time

class Solution:
    def combinationSum2(self, candidates, target):
        solutions = []
        currSolution = []
        self.buildSolution(candidates, target, currSolution, solutions)
        return solutions

    def buildSolution(self, candidates, target, currSolution, solutions):

        if target < 0:
            return
        
        if target == 0:
            currSolution.sort()
            if currSolution not in solutions:
                solutions.append(currSolution)
            return
        
        for i,_ in enumerate(candidates):
            candidatesCopy = candidates.copy()
            seenCandidate = candidatesCopy.pop(i)
            self.buildSolution(candidatesCopy, target-seenCandidate, currSolution + [seenCandidate], solutions)

    def test1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        res = self.combinationSum2(candidates, target)
        print("test1 res: ", res)

# s = Solution()
# s.test1()

""" Passes
Time complexity: O(2^n), where n ~ len(candidates). 2^n comes from the fact that you either 
    include a number or you don't include it in a combination.
Space complexity: O(n): recursion stack is at most O(n)
"""
class Solution2():
    def combinationSum2(self, candidates: [int], target: [int]) -> [[int]]:
        candidates.sort()
        solutions = []
        currSolution = []
        startIdx = 0
        self.buildSolution(candidates, target, currSolution, solutions, startIdx)
        return solutions

    
    def buildSolution(self, candidates, target, currSolution, solutions, startIdx):
        #print(f"target={target}, currSolution={currSolution}, startIdx={startIdx}")
        if target < 0:
            return

        if target == 0:
            currSolution.sort()
            if currSolution not in solutions:
                solutions.append(currSolution)
            return

        for i in range(startIdx, len(candidates)):
            c = candidates[i]
            if startIdx < i and candidates[i-1] == candidates[i]:
                continue
            #time.sleep(1)
            self.buildSolution(candidates, target - c, currSolution + [c], solutions, i+1)

    def test(self):
        cases = [
            dict(candidates=[10,1,2,7,6,1,5], target=8, expected=8),
            # dict(candidates=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
            #     target=27, expected=[])
        ]

        for case in cases:
            print("case: ", case)
            res = self.combinationSum2(case["candidates"], case["target"])
            print("res: ", res)
            assert res == case["expected"]

sol2 = Solution2()
sol2.test()