'''
https://leetcode.com/contest/weekly-contest-189/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
You have a very large square wall and a circular dartboard placed on the wall. 
You have been challenged to throw darts into the board blindfolded. 
Darts thrown at the wall are represented as an array of points on a 2D plane. 
Return the maximum number of points that are within or lie on any circular dartboard of radius r.
'''

class Solution:
    # TODO: not correct, need to figure out.
    def numPoints(self, points: List[List[int]], r: int) -> int:
        inside = []
        for i,point in enumerate(points):
            cen = self.getCentroid(points[:i+1])
            print("cen: ", cen)
            distFromCen = self.getDist(cen, point)
            if distFromCen <= r:
                inside.append(point)
        return len(inside)
    
    # returns (x,y) centroid
    def getCentroid(self, points):
        n = len(points)
        xSum = 0
        ySum = 0
        for i,point in enumerate(points):
            xSum += point[0]
            ySum += point[1]
        return (xSum/n, ySum/n)
    
    # between 2 points
    def getDist(self, p1, p2):
        dx = p2[0]-p1[0]
        dy = p2[1]-p1[1]
        return (dx**2 + dy**2)**(0.5)