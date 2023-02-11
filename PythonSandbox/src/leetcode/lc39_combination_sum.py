'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Time complexity: O(n^t), where n~len(candidates), t~target
Space complexity: O(t), t~target
'''
class Solution:
    def combinationSum(self, candidates, target):
        solutions = []
        currSolution = []
        self.buildSolution(candidates, target, currSolution, solutions)
        return solutions

    # helper function
    def buildSolution(self, candidates, target, currSolution, solutions):
        # print(f"target: {target}, currSolution: {currSolution}")
        if target < 0:
            return 

        if target == 0:
            currSolution.sort()
            if currSolution not in solutions:
                solutions.append(currSolution)
                # print("solutions updated: ", solutions)
            return
        
        for i in range(startIdx, len(candidates)):
            c = candidates[i]
            if i == startIdx or candidates[i-1] != c:
                self.buildSolution(candidates, target-c, currSolution+[c], solutions, i+1)

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