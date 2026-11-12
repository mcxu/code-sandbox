import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [] # minheap to store (dist, x, y)
        for p in points:
            d = self.dist(p)
            heapq.heappush(heap, (d, p[0], p[1]))
        
        output = []
        for _ in range(k):
            tup = heapq.heappop(heap)
            output.append([tup[1], tup[2]])
        return output

    def dist(self, point):
        x = point[0]; y = point[1]
        dist = ((x**2) + (y**2))**(1/2)
        return dist

    def test1(self):
        points = [[1,3],[-2,2]] 
        k = 1
        result = self.kClosest(points, k)
        print(f"{result=}")

    def test2(self):
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        result = self.kClosest(points, k)
        print(f"{result=}")


if __name__ == "__main__":
    s = Solution()
    s.test1()
    # s.test2()
