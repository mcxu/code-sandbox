# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        costUpTo = [float('inf')]*(len(cost))
        costUpTo[0] = cost[0]
        costUpTo[1] = cost[1]
        for i in range(2, len(cost)):
            costUpTo[i] = min(costUpTo[i-1], costUpTo[i-2]) + cost[i]
        #print("costUpTo: ", costUpTo)
        return min(costUpTo[-1], costUpTo[-2])