from typing import List
from collections import defaultdict

"""
https://leetcode.com/problems/graph-valid-tree/description/

Let V be the number of nodes and E is the number of edges.
Time complexity: O(V + E)
Space complexity: O(V + E)
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = self.buildAdjList(edges)
        print("adjList: ", adjList)
        
        startNode = min(adjList.keys()) if adjList else 0
        parent = None
        visited = set()
        currPath = set()
        hasLoop = self.checkLoop(startNode, parent, adjList, visited, currPath)
        if hasLoop:
            return False

        return len(visited) == n

    # dfs; True if there is a loop, False otherwise
    def checkLoop(self, node, parent, adjList, visited, currPath): # O(V + E) time, O(V) space bc of recursion depth V
        print("checkLoop: node: ", node, "parent: ", parent, "visited: ", visited, "currPath: ", currPath)
        if node in currPath:
            return True # there IS a loop
        if node in visited:
            return False # already visited

        currPath.add(node)

        for neighbor in adjList[node]:
            if neighbor == parent:
                continue
            hasLoop = self.checkLoop(neighbor, node, adjList, visited, currPath)
            print("hasLoop inside for loop: ", hasLoop)
            if hasLoop:
                return True
        
        currPath.remove(node)
        visited.add(node) # finally mark as visited once verified that there's no loop

        return False

    def buildAdjList(self, edges):
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        return adjList


    def test1(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        result = self.validTree(n, edges)
        print("result: ", result)
        assert result == True
    
    def test2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        result = self.validTree(n, edges)
        print("result: ", result)
        assert result == False
    
    def test3(self):
        n = 1
        edges = []
        result = self.validTree(n, edges)
        print("result: ", result)
        assert result == True

if __name__ == "__main__":
    s = Solution()
    # s.test1()
    # s.test2()
    s.test3()
