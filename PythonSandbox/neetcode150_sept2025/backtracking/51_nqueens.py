class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)] 
        #print("board:\n", board)
        rowIdx = 0
        cols = set()
        posDiag = set()
        negDiag = set()
        results = []
        self.dfs(n, board, rowIdx, cols, posDiag, negDiag, results)
        return results
    
    def dfs(self, n, board, rowIdx, cols, posDiag, negDiag, results):
        if rowIdx == n:
            boardSnapshot = ["".join(r) for r in board]
            results.append(boardSnapshot)
            return
        
        for colIdx in range(n):
            #print("rowIdx: ", rowIdx, "    colIdx: ", colIdx)
            if colIdx in cols or (rowIdx+colIdx) in posDiag or (rowIdx-colIdx) in negDiag:
                continue
            
            cols.add(colIdx)
            posDiag.add(rowIdx+colIdx)
            negDiag.add(rowIdx-colIdx)
            board[rowIdx][colIdx] = "Q"
            
            self.dfs(n, board, rowIdx+1, cols, posDiag, negDiag, results)

            cols.remove(colIdx)
            posDiag.remove(rowIdx+colIdx)
            negDiag.remove(rowIdx-colIdx)
            board[rowIdx][colIdx] = "."
        return


    def test1(self):
        result = self.solveNQueens(4)
        print("result:\n", result)

if __name__ == "__main__":
    s = Solution()
    s.test1()
    