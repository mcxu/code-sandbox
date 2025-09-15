"""
https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
"""

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        output = [[0 for _ in grid[0]] for _ in grid]
        # print('output: ', output)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # print(f"row:{r}, col:{c}")
                topLeftDistVals = self.getNumDistinctVals(grid, r, c, True)
                botRightDistVals = self.getNumDistinctVals(grid, r, c, False)
                output[r][c] = abs(topLeftDistVals - botRightDistVals)
                
        return output
    
    def getNumDistinctVals(self, grid, r, c, direction):
        vals = set()
        
        if direction == True: # top left
            r -= 1; c -= 1
            while r >= 0 and c >= 0:
                vals.add(grid[r][c])
                r -= 1; c -= 1
        else: # bottom right
            r += 1; c += 1
            while r <= len(grid)-1 and c <= len(grid[0])-1:
                vals.add(grid[r][c])
                r += 1; c += 1
        
        return len(vals)
    