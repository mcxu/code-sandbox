# https://leetcode.com/problems/maximal-network-rank/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjList = self.createAdjList(n, roads)
        
        maxNR = -float('inf')
        for fr in range(n):
            for to in range(fr+1, n):
                fromList = adjList[fr]
                toList = adjList[to]
                connections = len(fromList) + len(toList)
                if fr in toList and to in fromList:
                    connections -= 1
                
                maxNR = max(maxNR, connections)
        
        return maxNR
    
    def createAdjList(self, n, roads):
        adjList = {}
        for i in range(n):
            adjList[i] = []
        
        for i,road in enumerate(roads):
            fr = road[0]
            to = road[1]
            adjList[fr].append(to)
            adjList[to].append(fr)
        return adjList