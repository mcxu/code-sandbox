'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Time complexity: O(n^t), where n~len(candidates), t~target
Space complexity: O(t), t~target
'''
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        currSolution = []
        solutions = []
        # call recursive function
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
        
        for i in range(0, len(candidates)):
            c = candidates[i]
            self.buildSolution(candidates, target-c, currSolution+[c], solutions)

    def test1(self):
        candidates = [2,3,6,7]
        target = 7
        res = self.combinationSum(candidates, target)
        print("test1 res: ", res)
    
    def test2(self):
        candidates = [2,3,5]
        target = 8
        res = self.combinationSum(candidates, target)
        print("test2 res: ", res)
    
s = Solution()
s.test1()
#s.test2()