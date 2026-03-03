# https://leetcode.com/problems/sliding-puzzle/
from copy import deepcopy

class Solution:
    def slidingPuzzle(self, board: [[int]]) -> int:
        solvedState = [[1,2,3],[4,5,0]]
        
        # # find 0 in given board
        zeroCoord = (-1,-1)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x]==0:
                    zeroCoord = (y,x)
                    break
        
        q = [(deepcopy(board),zeroCoord,0)]
        leastMoves = float('inf')
        visited = set()
        while q:
            qItem = q.pop(0)
            #print("-- qItem: ", qItem)
            #print("q remaining: ", q)
            currState = qItem[0]
            currZeroCoord = qItem[1]
            currDepth = qItem[2]
            
            # generate str from currState
            stateHash = ""
            for y in range(len(currState)):
                for x in range(len(currState[0])):
                    stateHash += str(currState[y][x])
            #print("stateHash: ", stateHash)
            #print("visited: ", visited)
            if stateHash not in visited:
                # add stateHash to visitedStates
                visited.add(stateHash)
                #print("added to visited: ", visited)
                # check if current state matches solvedState
                if currState==solvedState and currDepth<leastMoves:
                    leastMoves = currDepth
                    #print("leastMoves updated: ", leastMoves)

                # possible moves onto q
                zy,zx = currZeroCoord
                movesList = [[0,-1],[-1,0],[0,1],[1,0]] # deltas
                for dy,dx in movesList:
                    py,px = [zy+dy, zx+dx]
                    #print("py,px: ", py, px)
                    if py<0 or py>len(board)-1 or px<0 or px>len(board[0])-1:
                        continue
                    self.swap(currState, (zy,zx), (py,px))
                    newqItem = (deepcopy(currState), (py,px), currDepth+1)
                    #print("newqItem: ", newqItem)
                    q.append(newqItem)
                    self.swap(currState, (zy,zx), (py,px))
        
        return leastMoves if leastMoves != float('inf') else -1
        
    
    # a, b are coordinates in format (y,x)
    def swap(self, board, a, b):
        ay,ax = a
        by,bx = b
        board[ay][ax],board[by][bx]=board[by][bx],board[ay][ax]