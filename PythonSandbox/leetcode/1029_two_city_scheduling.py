'''
https://leetcode.com/problems/two-city-scheduling/
'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0]-x[1])
        #print("costs sorted: ", costs)
        minCost=0
        for i in range(len(costs)): 
            if i < len(costs)/2:
                minCost += costs[i][0] # choose A
            else:
                minCost += costs[i][1] # choose B
        #print("minCost: ", minCost)
        return minCost