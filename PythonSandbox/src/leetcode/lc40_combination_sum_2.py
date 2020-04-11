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
class Solution:
    def combinationSum2(self, candidates, target):
        solutions = []
        self.helper(candidates, target, [], solutions)
        #print("solutions: ", solutions)
        return solutions
        
    def helper(self, candidates, target, sol, solutions):
        #print("candidates: ", candidates)
        #print("sol: ", sol)
        if target < 0:
            return 
        
        if target == 0:
            sortedSol = sorted(sol)
            if sortedSol not in solutions:
                solutions.append(sortedSol)
            return
        
        #print("start of for loop for candidates: ", candidates)
        for i in range(len(candidates)):
            candidatesCopy = candidates.copy()
            cand = candidatesCopy.pop(i)
            self.helper(candidatesCopy, target-cand, sol+[cand], solutions)
        
    def test1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        res = self.combinationSum2(candidates, target)
        print("test1 res: ", res)

s = Solution()
s.test1()