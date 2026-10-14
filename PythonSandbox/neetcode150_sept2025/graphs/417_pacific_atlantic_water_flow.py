from typing import List

"""
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Time complexity: O((r * c)^2) where r is the number of rows and c is the number of columns.
    The iteration through the matrix is O(r * c), and the recursive dfs is O(r * c) for each cell.
    Therefore, the time complexity is O((r * c)^2).
Space complexity: O(r * c) for the visited set.
    The visited set is used to avoid revisiting the same cell along the path from a starting cell.
    Therefore, the space complexity is O(r * c).
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                visited = set()
                canReachPacific, canReachAtlantic = self.canReachBothSeas(heights, r, c, visited)
                #print("r:", r, "c:", c, "val:", heights[r][c], "canReachP:", canReachPacific, "canReachA:", canReachAtlantic, "\tboth:", canReachPacific & canReachAtlantic)
                if canReachPacific and canReachAtlantic:
                    result.append([r, c])
        return result

    # dfs
    def canReachBothSeas(self, heights, r, c, visited):
        if (r, c) in visited:
            return (False, False)

        visited.add((r, c))

        canReachPacific = (r <= 0 or c <= 0)
        canReachAtlantic = (r >= len(heights) - 1 or c >= len(heights[0]) - 1)

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newr, newc = r + dr, c + dc
            withinBounds = 0 <= newr <= len(heights)-1 and 0 <= newc <= len(heights[0])-1
            if withinBounds and heights[newr][newc] <= heights[r][c]:
                p, a = self.canReachBothSeas(heights, newr, newc, visited)
                canReachPacific |= p
                canReachAtlantic |= a

        return (canReachPacific, canReachAtlantic)
        

    def test1(self):
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        expected =  [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        result = self.pacificAtlantic(heights)
        print("result: ", result)
        assert set([tuple(tup) for tup in result]) == \
            set([tuple(tup) for tup in expected])
    
    def test2(self):
        heights = [[1]]
        expected = [[0,0]]
        result = self.pacificAtlantic(heights)
        print("result: ", result)
        assert set([tuple(tup) for tup in result]) == \
            set([tuple(tup) for tup in expected])

if __name__ == "__main__":
    s = Solution()
    s.test1()
    # s.test2()

