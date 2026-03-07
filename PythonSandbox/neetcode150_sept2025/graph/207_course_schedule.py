from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True
        
        adjList = self.buildAdjList(prerequisites)
        print("adjList: ", adjList)
        visited = set()

        for course in range(numCourses):
            print("course: ", course)
            currPath = set()
            nodeCycleFree = self.dfs(course, adjList, visited, currPath)
            print("nodeCycleFree: ", nodeCycleFree)
            if not nodeCycleFree:
                return False # cycle detected in node

        return True

    def dfs(self, node, adjList, visited, currPath):
        if node in currPath:
            return False # cycle detected
        if node in visited: 
            return True # already visited
        
        currPath.add(node)

        for prereq in adjList[node]:
            print("prereq: ", prereq)
            neighborsCycleFree = self.dfs(prereq, adjList, visited, currPath)
            if not neighborsCycleFree:
                return False # cycle detected in neighbor
        
        currPath.remove(node)
        visited.add(node) # means node and its prerequisites are fully traversed and no cycle detected

        return True

    def buildAdjList(self, edges) -> {}: 
        adjList = defaultdict(list)
        for course, prereq in edges:
            adjList[course].append(prereq)
        return adjList

    
    def test1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        result = self.canFinish(numCourses, prerequisites)
        print("result: ", result)

    def test2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        result = self.canFinish(numCourses, prerequisites)
        print("result: ", result)

if __name__ == "__main__":
    s = Solution()
    s.test1()
    # s.test2()