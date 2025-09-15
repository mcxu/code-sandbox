"""
https://leetcode.com/problems/combination-sum-iii/description/
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        solutions = []
        currSolution = []
        idx = 1
        self.buildSolution(k, n, currSolution, solutions, idx)
        return solutions
    
    def buildSolution(self, k, n, currSolution, solutions, idx):
        
        if n < 0:
            return

        if n == 0 and k == 0:
            currSolution.sort()
            if currSolution not in solutions:
                solutions.append(currSolution)
            return

        for i in range(idx, 10):
            self.buildSolution(k-1, n-i, currSolution + [i], solutions, i+1)

