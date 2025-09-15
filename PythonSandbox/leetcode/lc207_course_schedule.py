'''
https://leetcode.com/problems/course-schedule/description/
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        adjList = self.buildAdjList(numCourses, prerequisites)
        print("adjList: ", adjList)
        if len(adjList) == 0:
            return True
        
        visited = set() # stores visited nodes

        canFin = True
        for startingCourse in range(len(adjList)):
            print("================= startingCourse: ", startingCourse)
            canFin &= self.mapDfs(startingCourse, adjList, visited)
            if not canFin:
                return False
            print("visitedAfter: ", visited)

        return canFin
        
    
    def mapDfs(self, courseIdx, adjList, visited):
        print("--- mapDfs ---")
        print(f"courseIdx: {courseIdx}, visited: {visited}")
        if courseIdx in visited:
            print("courseIdx in visited, returning False")
            return False
        
        if courseIdx in adjList.keys():
            visited.add(courseIdx)
            print("visited updated: ", visited)

            prereqs = adjList[courseIdx]
            print("prereqs: ", prereqs)
            
            resultFromThisCourse = True

            if adjList[courseIdx] == []:
                resultFromThisCourse = True

            prereqs = adjList[courseIdx]
            # print("prereqs: ", prereqs)
            
            for pidx in prereqs:
                resultFromThisCourse &= self.mapDfs(pidx, adjList, visited)
                if not resultFromThisCourse:
                    return False
            
            visited.remove(courseIdx)
            adjList[courseIdx] = []

            print(f"For courseIdx: {courseIdx}, resultFromThisCourse: {resultFromThisCourse}")
            print(f"adjList before returning: ", adjList)
            return resultFromThisCourse

        return False

        
    def buildAdjList(self, numCourses, prereqs):
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
            for item in prereqs:
                course, pre = item[0], item[1]
                if i == course:
                    adjList[course].append(pre)
        return adjList
    

    def test(self):
        cases = [
            # dict(numCourses=5, prerequisites=[[1,4],[2,4],[3,1],[3,2]], expected=True),
            # dict(numCourses=3, prerequisites=[[2,1],[1,0]], expected=True)
            # dict(numCourses=3, prerequisites=[[1,0],[1,2],[0,1]], expected=False),
            #dict(numCourses=20, prerequisites=[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]], expected=False)
            dict(numCourses=5, prerequisites=[[1,4],[2,4],[3,1],[3,2]])
        ]

        for case in cases:
            print(f"Case: {case}")
            numCourses = case["numCourses"]
            prerequisites = case["prerequisites"]
            expected = case["expected"]

            res = self.canFinish(numCourses, prerequisites)
            print("result: ", res)
            assert res == expected

sol = Solution()
sol.test()



