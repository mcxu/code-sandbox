'''
https://leetcode.com/problems/number-of-islands/
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        #print("visited: ", visited)
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and visited[y][x] == False:
                    self.floodFillIsland(grid, y, x, visited)
                    count += 1
        
        return count

    
    def floodFillIsland(self, grid, y, x, visited):
        if y < 0 or y > len(grid)-1 or x < 0 or x > len(grid[0])-1:
            return 

        if grid[y][x] == "0" or visited[y][x] == True:
            return
            
        visited[y][x] = True # fill current cell
        self.floodFillIsland(grid, y-1, x, visited)
        self.floodFillIsland(grid, y, x-1, visited)
        self.floodFillIsland(grid, y+1, x, visited)
        self.floodFillIsland(grid, y, x+1, visited)
        return 
        