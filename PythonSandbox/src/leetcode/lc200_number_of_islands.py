'''
https://leetcode.com/problems/number-of-islands/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] 
                   for _ in range(len(grid))]
        numIslands = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if visited[y][x] == False and grid[y][x] == "1":
                    self.dfs(y, x, grid, visited)
                    numIslands += 1
                else:
                    visited[y][x] = True
        return numIslands
    
    def dfs(self, y, x, grid, visited):
        if y<0 or y>len(grid)-1 or x<0 or x>len(grid[0])-1:
            return
        elif grid[y][x] == "0" or visited[y][x]==True:
            return
        
        visited[y][x] = True
        self.dfs(y, x+1, grid, visited)
        self.dfs(y, x-1, grid, visited)
        self.dfs(y-1, x, grid, visited)
        self.dfs(y+1, x, grid, visited)