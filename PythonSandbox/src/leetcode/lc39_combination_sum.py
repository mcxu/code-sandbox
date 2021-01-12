'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/
'''
class Solution:
    '''

    '''
    def combinationSum(self, candidates, target):
        solutions = []
        self.helper(candidates, target, [], solutions)
        #print("solutions: ", solutions)
        return solutions
    
    def helper(self, candidates, target, sol, solutions):
        #print("sol: ", sol)
        if target < 0:
            return
        
        if target == 0:
            sortedSol = sorted(sol)
            if sortedSol not in solutions:
                solutions.append(sortedSol)
            return
        
        for i in range(len(candidates)):
            c = candidates[i]
            self.helper(candidates, target-c, sol+[c], solutions)

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