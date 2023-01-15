'''
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
'''
class Solution:
    def maxNonOverlapping(self, nums: [int], target: int) -> int:
        cSum = 0
        sol = 0
        diffMap = {0:-1} # maps cSum-target: index
        lastInd = diffMap[0]
        for i,n in enumerate(nums):
            print("--- i=", i)
            cSum += n
            diff = cSum-target
            print("cSum: ", cSum)
            print("diff: ", diff)
            print("diffMap: ", diffMap)
            if diff in diffMap.keys() and diffMap[diff] >= lastInd:
                lastInd = i
                sol+=1
                diffMap.clear() # don't need previous indices anymore
            print("lastInd: ", lastInd)
            print("sol: ", sol)
            diffMap[cSum] = i
        return sol
    
    def test1(self):
        #nums = [1,1,1,1]
        nums = [1,1,1,1,1]
        #target = 1
        target = 2
        #target = 3
        res = self.maxNonOverlapping(nums, target)
        print("res: ", res)
    
    def test2(self):
        # explains why init map with {0:-1}. Because if the num itself == target,
        # then lastInd must be updated to curr index, the 1st of which is 0.
        nums = [0,0,0]
        target = 0
        res = self.maxNonOverlapping(nums, target)
        print("res: ", res)

s = Solution()
s.test1()
#s.test2()
