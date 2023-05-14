"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
"""

from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        overallMax = 0
        memo = {}

        for row in range(len(grid)):
            maxLengthPath = self.walk(grid, row, 0, memo)
            overallMax = max(overallMax, maxLengthPath)
        
        return overallMax
    
    def walk(self, grid, row, col, memo):
        if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1:
            return 0
        
        currVal = grid[row][col]
        
        rcTup = (row, col)
        if rcTup in memo.keys():
            return memo[rcTup]

        upRight = 0
        right = 0
        downRight = 0
        
        # test up-right
        if row - 1 >= 0 and col + 1 < len(grid[0]) and grid[row-1][col+1] > currVal:
            upRight = 1 + self.walk(grid, row-1, col+1, memo)
        
        # test right
        if col + 1 < len(grid[0]) and grid[row][col+1] > currVal:
            right = 1 + self.walk(grid, row, col+1, memo)
        
        # test down-right 
        if row + 1 < len(grid) and col + 1 < len(grid[0]) and grid[row+1][col+1] > currVal:
            downRight = 1 + self.walk(grid, row+1, col+1, memo)
        
        memo[rcTup] = max([upRight, right, downRight]) # maxLengthPath
        return memo[rcTup]
        