'''
https://leetcode.com/problems/minimum-path-sum/
'''
import unittest

class Solution(unittest.TestCase):
    def minPathSum(self, grid: [[int]]) -> int:
        if not grid:
            return 0
        
        aux = [[0 for _ in range(len(grid[0]))] 
               for _ in range(len(grid))]
        aux[0][0] = grid[0][0]
        for y in range(1, len(grid)):
            aux[y][0] = aux[y-1][0] + grid[y][0]
        for x in range(1, len(grid[0])):
            aux[0][x] = aux[0][x-1] + grid[0][x]
            
        for y in range(1, len(grid)):
            for x in range(1, len(grid[0])):
                aux[y][x] += min(grid[y][x] + aux[y-1][x],
                                grid[y][x] + aux[y][x-1])
        return aux[-1][-1]
    
    def test1(self):
        grid = [[1,3,1],
                [1,5,1],
                [4,2,1]]
        res = self.minPathSum(grid)
        self.assertEqual(res, 7)

unittest.main()
        