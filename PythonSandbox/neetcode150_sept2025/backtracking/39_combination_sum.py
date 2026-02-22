from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        startIdx = 0
        currSolution = []
        self.backtrack(candidates, target, startIdx, currSolution, solutions)
        return solutions
    
    def backtrack(self, candidates, target, startIdx, currSolution, solutions):
        if target == 0:
            solutions.append(currSolution.copy())
            return
        
        if target < 0:
            return
        
        for i in range(startIdx, len(candidates)):
            currSolution.append(candidates[i])
            self.backtrack(candidates, target-candidates[i], i, currSolution, solutions)
            currSolution.pop()
    
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

if __name__ == "__main__":
    sol = Solution()
    sol.test1()
    #sol.test2()