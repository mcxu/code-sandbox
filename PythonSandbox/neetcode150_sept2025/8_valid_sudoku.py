from typing import List

class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for row in board:
            seen = set()
            for rowNum in row:
                if rowNum != ".":
                    if rowNum in seen:
                        return False
                    else:
                        seen.add(rowNum)

        # # check all cols
        for x in range(len(board[0])):
            seen = set()
            for y in range(len(board)):
                colNum = board[y][x]
                if colNum != ".":
                    if colNum in seen:
                        return False
                    else:
                        seen.add(colNum)

        # check all boxes
        xBounds = [3, 6, 9]
        yBounds = [3, 6, 9]
        for yb in yBounds:
            for xb in xBounds:
                # print(f"yb:{yb}, xb:{xb}")
                seen = set()
                for y in range(yb-3, yb, 1):
                    for x in range(xb-3, xb, 1):
                        # print(f"y={y}, x={x}")
                        sqNum = board[y][x]
                        if sqNum != ".":
                            if sqNum in seen:
                                return False
                            else:
                                seen.add(sqNum)

        return True


    def test_1(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

        output = self.isValidSudoku(board)
        print("ouput: ", output)


if __name__ == "__main__":
    cl = ValidSudoku()
    cl.test_1()