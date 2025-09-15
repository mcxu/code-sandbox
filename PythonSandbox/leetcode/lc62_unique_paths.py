# https://leetcode.com/problems/unique-paths/
class Solution: 
    """ dynamic programming 
    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[-1][-1]

class Solution2: 
    """ recursive + memoization
    Time complexity: O(n) with memo, O(2^n) without memo
    Space complexity: 
        With memo: pathMemo is O(m*n) + recursion stack is O(m*n) = overall O(m*n)
        Without memo: recursion stack is O(m*n) = overall O(m*n)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        pathMemo = {}
        paths = self.dfs(m, n, pathMemo)
        return paths

    def dfs(self, row, col, pathMemo):

        ''' This if-statement is the important part to understand.
        '''
        if row == 0 and col == 0:
            return 0

        if row == 1 or col == 1:
            return 1

        if (row, col) in pathMemo.keys():
            return pathMemo[(row, col)]

        moveUp = self.dfs(row - 1, col, pathMemo)
        moveLeft = self.dfs(row, col - 1, pathMemo)

        pathMemo[(row, col)] = moveUp + moveLeft
        return pathMemo[(row, col)]