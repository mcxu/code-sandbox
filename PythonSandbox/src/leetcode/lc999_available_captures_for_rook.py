'''
https://leetcode.com/problems/available-captures-for-rook/
'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # located rook
        rookStart = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    rookStart = (i,j)
                    break
        
        nUp = self.moveRook(board, rookStart, "up")
        nDown = self.moveRook(board, rookStart, "down")
        nLeft = self.moveRook(board, rookStart, "left")
        nRight = self.moveRook(board, rookStart, "right")
        return nUp + nDown + nLeft + nRight

    def moveRook(self, board, rookStart, direction):
        npawns = 0
        i = rookStart[0]
        j = rookStart[1]
        while board[i][j] != "B":
            if board[i][j] == "p":
                npawns += 1
                break
            
            if direction == "up":
                i -= 1
            elif direction == "down":
                i += 1
            elif direction == "left":
                j -= 1
            elif direction == "right":
                j += 1
                
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                break
                
        return npawns