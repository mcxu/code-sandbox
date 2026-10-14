from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        maxArea = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                #print(f"curr coord: y:{y}, x:{x}, num: {grid[y][x]}")
                if grid[y][x] != 0 and visited[y][x] == False:
                    #print(f"dfs begin: y:{y}, x:{x}")
                    area = self.getArea(grid, y, x, visited)
                    maxArea = max(maxArea, area)
        return maxArea

    def getArea(self, grid, y, x, visited):
        if not (0 <= y < len(grid)) or not (0 <= x < len(grid[0])):
            return 0
        
        if grid[y][x] == 0 or visited[y][x] == True:
            return 0

        visited[y][x] = True
        
        currArea = grid[y][x]
        currArea += self.getArea(grid, y-1, x, visited)
        currArea += self.getArea(grid, y, x+1, visited)
        currArea += self.getArea(grid, y+1, x, visited)
        currArea += self.getArea(grid, y, x-1, visited)
        return currArea

    def test1(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        expectedOutput = 6
        area = self.maxAreaOfIsland(grid)
        print("area(test): ", area)
    
    def test_getArea(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        y = 3
        x = 4
        visited = [[False for _ in grid[0]] for _ in grid]
        area = self.getArea(grid, y, x, visited)
        print("area: ", area)

if __name__ == "__main__":
    s = Solution()
    s.test1()
    # s.test_getArea()


