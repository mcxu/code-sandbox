'''
https://leetcode.com/problems/number-of-islands/
'''
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))]
                    for _ in range(len(grid))]
        
        numIslands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and visited[y][x] == False:
                    self.dfs(y, x, grid, visited)
                    numIslands += 1
        return numIslands


    # flood fill
    def dfs(self, y, x, grid, visited):
        if y<0 or y>=len(grid) or x<0 or x>=len(grid[0]):
            return
        
        if grid[y][x] == "0" or visited[y][x] == True:
            return
        
        visited[y][x] = True            # fill current
        self.dfs(y, x+1, grid, visited) # fill right
        self.dfs(y, x-1, grid, visited) # fill left
        self.dfs(y-1, x, grid, visited) # fill top
        self.dfs(y+1, x, grid, visited) # fill down