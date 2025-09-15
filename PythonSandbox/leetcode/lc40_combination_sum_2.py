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
from typing import List

""" Passes
Time complexity: O(2^n), where n ~ len(candidates). 2^n comes from the fact that you either 
    include a number or you don't include it in a combination.
Space complexity: O(n): recursion stack is at most O(n)
"""
class Solution2():
    def combinationSum2(self, candidates: List[int], target: List[int]) -> List[List[int]]:
        candidates.sort() # need this so that same nums are next to each other
        solutions = []
        currSolution = []
        startIdx = 0
        self.buildSolution(candidates, target, currSolution, solutions, startIdx)
        return solutions

    def buildSolution(self, candidates, target, currSolution, solutions, startIdx):
        # print(f"candidates: {candidates}, target: {target}, currSol: {currSolution}, solutions: {solutions}, startIdx: {startIdx}")        
        if target < 0:
            return

        if target == 0:
            currSolution.sort()
            if currSolution not in solutions:
                solutions.append(currSolution)
            return

        for i in range(startIdx, len(candidates)):
            c = candidates[i]
            if i == startIdx or candidates[i-1] != candidates[i]:
                self.buildSolution(candidates, target - c, currSolution + [c], solutions, i+1)

    def test(self):
        cases = [
            dict(candidates=[10,1,2,7,6,1,5], target=8, expected=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
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

# ===============================================================================

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

