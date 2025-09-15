'''
https://leetcode.com/problems/island-perimeter/
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in grid[0]] for _ in grid]
        perim = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x]==1 and visited[y][x]==0:
                    perim = self.getPerim(grid, y, x, visited)
                    break
        return perim
        
    
    def getPerim(self, grid, y, x, visited):
        if y < 0 or y > len(grid)-1 or x < 0 or x > len(grid[0])-1:
            return 1
        
        if visited[y][x]==1:
            return 0
        
        if grid[y][x]==0:
            return 1
        
        visited[y][x] = 1
        perimUp = self.getPerim(grid, y-1, x, visited)
        perimDown = self.getPerim(grid, y+1, x, visited)
        perimLeft = self.getPerim(grid, y, x-1, visited)
        perimRight = self.getPerim(grid, y, x+1, visited)
        return perimUp + perimDown + perimLeft + perimRight