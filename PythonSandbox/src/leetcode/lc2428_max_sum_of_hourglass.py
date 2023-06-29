from typing import List

class Solution:
    

    def maxSum(self, grid: List[List[int]]) -> int:        
        
        maxSum = 0

        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                rcSum = self.getHourglassSum(grid, r, c)
                maxSum = max(maxSum, rcSum)
        
        return maxSum

    def getHourglassSum(self, grid, r, c):
        # r,c is topLeft
        topLeft = grid[r][c]
        topMid = grid[r][c+1]
        topRight = grid[r][c+2]
        mid = grid[r+1][c+1]
        botLeft = grid[r+2][c]
        botMid = grid[r+2][c+1]
        botRight = grid[r+2][c+2]
        return sum([topLeft, topMid, topRight, mid, botLeft, botMid, botRight])
