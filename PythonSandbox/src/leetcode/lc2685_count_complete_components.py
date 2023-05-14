"""
https://leetcode.com/problems/count-the-number-of-complete-components/description/
"""

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        if not edges:
            return n

        adjList = self.buildAdjList(edges, n)
        currNode = min(adjList.keys())
        completeComponents = 0
        visitedRef = set(adjList.keys()).copy()

        while len(visitedRef) > 0:
            refSet = set([currNode] + adjList[currNode])
            visited = set()
            isClique = self.checkClique(adjList, currNode, refSet, visited)
            completeComponents += 1 if isClique else 0
            
            visitedRef -= visited
            if not visitedRef:
                break

            currNode = min(visitedRef)

        return completeComponents
    
    
    def checkClique(self, adjList, currNode, refSet, visited):
        if currNode not in visited:
            visited.add(currNode)

        # validate connections
        neighbors = adjList[currNode]
        newRefSet = set([currNode] + neighbors)

        if refSet != newRefSet:
            return False

        neighborsAreClique = True

        for nbr in adjList[currNode]:
            if nbr not in visited:
                neighborsAreClique &= self.checkClique(adjList, nbr, refSet, visited)
        
        return neighborsAreClique

    def buildAdjList(self, edges, n):
        adjList = {}
        for i in range(len(edges)):
            e = edges[i]
            fr,to = e[0],e[1]

            if fr not in adjList.keys():
                adjList[fr] = [to]
            else:
                adjList[fr].append(to)
            
            if to not in adjList.keys():
                adjList[to] = [fr]
            else:
                adjList[to].append(fr)

        # fill in any missing vertices
        for i in range(n):
            if i not in adjList.keys():
                adjList[i] = []

        return adjList