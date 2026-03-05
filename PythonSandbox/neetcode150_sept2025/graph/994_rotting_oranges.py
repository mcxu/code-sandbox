from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        fresh = 0
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]
                if val == 1:
                    fresh += 1
                elif val == 2:
                    queue.append((r,c))
        
        if fresh == 0:
            return 0
        
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    newr, newc = r+dr, c+dc
                    if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc]==1:
                        grid[newr][newc] = 2
                        fresh -= 1
                        queue.append((newr, newc))
            time += 1
        
        # print("fresh: ", fresh)
        # print("time: ", time)

        return time if fresh == 0 else -1
    
    def test1(self):
        grid = [[2,1,1],
                [1,1,0],
                [0,1,1]]
        expectedOutput = 4
        output = self.orangesRotting(grid)
        print("output: ", output)
        if output == expectedOutput:
            print("Test passed")
        else:
            print("Test failed")

if __name__ == "__main__":
    s = Solution()
    s.test1()


"""
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        fresh = 0
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]
                if val == 1:
                    fresh += 1
                elif val == 2:
                    queue.append((r,c))
        
        if fresh == 0:
            return 0
        
        time = 0
        while queue and fresh > 0:
            r,c = queue.pop(0)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                newr, newc = r+dr, c+dc
                if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc]==1:
                    grid[newr][newc] = 2
                    fresh -= 1
                    append((newr), (newc))
            time += 1
        
        return time if time >= 0 else -1
"""