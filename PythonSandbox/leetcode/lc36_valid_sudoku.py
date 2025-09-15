# https://leetcode.com/problems/valid-sudoku/submissions/941373419/

from typing import List

class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            rowSet = set(); colSet = set(); sqSet = set()

            # print("BEGIN ROW: ", row)
            valid = True

            for col in range(len(board[0])):
                #print(f"    row:{row}, col:{col}")

                # validate row
                rowVal = board[row][col]
                if rowVal.isnumeric():
                    if int(rowVal) not in rowSet:
                        rowSet.add(int(rowVal))
                    else:
                        return False

                # validate col
                colVal = board[col][row]
                if colVal.isnumeric():
                    if int(colVal) not in colSet:
                        colSet.add(int(colVal))
                    else:
                        return False

                # validate sub-square
                ssRow =  (row // 3) * 3 + (col // 3)
                ssCol = (row % 3) * 3 + (col % 3)
                # print(f"    row:{row}, col:{col}, ssRow: {ssRow}, ssCol: {ssCol}")
                ssVal = board[ssRow][ssCol]
                if ssVal.isnumeric():
                    if int(ssVal) not in sqSet:
                        sqSet.add(int(ssVal))
                    else:
                        return False

        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.isValidArr(row) == False:
                return False
        
        for x in range(len(board[0])):
            colArr = []
            for y in range(len(board)):
                colArr.append(board[y][x])
            if self.isValidArr(colArr)==False:
                return False
        
        stopInds = [2,5,8]
        for sy in stopInds:
            for sx in stopInds:
                starty = sy-2
                startx = sx-2
                innerArr = []
                for y in range(starty, sy+1):
                    for x in range(startx, sx+1):
                        innerArr.append(board[y][x])
                if self.isValidArr(innerArr)==False:
                    return False
        return True
                
    
    def isValidArr(self, arr):
        numSet = set([i for i in range(1,10)])
        for i,n in enumerate(arr):
            if n != ".":
                nint = int(n)
                if nint in numSet:
                    numSet.remove(nint)
                else:
                    return False
        return True