from typing import List
from collections import defaultdict

"""
https://leetcode.com/problems/course-schedule/description/

Let V be the number of courses and E is the number of prerequisites.
Time complexity: O(V + E)
Space complexity: O(V + E)
"""

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
            cycleExists = self.checkCycle(course, adjList, visited, currPath)
            print("cycleExists: ", cycleExists)
            if cycleExists:
                return False # cycle detected in node

        return True

    # dfs; True if there is a cycle, False otherwise
    def checkCycle(self, node, adjList, visited, currPath):
        if node in currPath:
            return True # cycle detected
        if node in visited: 
            return False # already visited
        
        currPath.add(node)

        for prereq in adjList[node]:
            print("prereq: ", prereq)
            cycleExists = self.checkCycle(prereq, adjList, visited, currPath)
            if cycleExists:
                return True # cycle detected in neighbor
        
        currPath.remove(node)
        visited.add(node) # means node and its prerequisites are fully traversed and no cycle detected

        return False

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