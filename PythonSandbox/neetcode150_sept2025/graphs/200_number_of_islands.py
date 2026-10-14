from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]

        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and visited[y][x] == False:
                    self.floodFill(grid, y, x, visited)
                    count += 1
        
        return count
    
    def floodFill(self, grid, y, x, visited):
        if not (0 <= y < len(grid)) or not (0 <= x < len(grid[0])):
            return

        if grid[y][x] == "0" or visited[y][x] == True:
            return
        
        visited[y][x] = True
        self.floodFill(grid, y-1, x, visited)
        self.floodFill(grid, y, x+1, visited)
        self.floodFill(grid, y+1, x, visited)
        self.floodFill(grid, y, x-1, visited)
        return

