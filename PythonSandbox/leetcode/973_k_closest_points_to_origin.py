'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''
class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        distMap = {} # stores: dist:[point] (list b/c there may be more than 1 point with the same dist)

        for point in points:
            d = self.dist(point)
            if d not in distMap.keys():
                distMap[d] = [point]
            else:
                distMap[d].append(point)
        
        out = []
        count = 0
        distSorted = sorted(distMap.keys())
        for dist in distSorted:
            pointsForDist = distMap[dist]
            for point in pointsForDist:
                if count < K:
                    out.append(point)
                    count += 1
        return out

    # dist from origin
    def dist(self, point):
        d = (point[0]**2 + point[1]**2)**(1/2)
        return d
    
    def test1(self):
        points = [[1,3],[-2,2]]
        K = 1
        # expected: [[-2,2]]
        res = self.kClosest(points, K)
        print("test1 res: ", res)

    def test2(self):
        points = [[3,3],[5,-1],[-2,4]]
        K = 2
        # expected: [[3,3],[-2,4]] (The answer [[-2,4],[3,3]] would also be accepted.)
        res = self.kClosest(points, K)
        print("test2 res: ", res)

s = Solution()
#s.test1()
s.test2()