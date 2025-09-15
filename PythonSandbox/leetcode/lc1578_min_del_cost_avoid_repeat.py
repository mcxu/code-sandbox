'''
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/submissions/
'''

class Solution:
    def minCost(self, s: str, cost: [int]) -> int:
        tc = 0
        p = 0 # store index of previously "deleted" char
        for i in range(1, len(s)):
            if s[p]==s[i]:
                tc += min(cost[p], cost[i])
                if cost[i] > cost[p]:
                    p = i
            else:
                p = i
            
        return tc

    def test1(self):
        s = "abaac" 
        cost = [1,2,3,4,5]
        mc = self.minCost(s, cost)
        print("mc: ", mc)

    def test2(self):
        s = "abc"
        cost = [1,2,3]
        mc = self.minCost(s, cost)
        print("mc: ", mc)

    def test3(self):
        s = "aabaa"
        cost = [1,2,3,4,1]
        mc = self.minCost(s, cost)
        print("mc: ", mc)

s = Solution()
#s.test1()
s.test2()
#s.test3()