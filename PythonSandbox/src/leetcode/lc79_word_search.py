'''
79. Word Search (https://leetcode.com/problems/word-search/)
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
'''
class Solution:
    # Time Limit Exceeded, but correct.
    def exist(self, board, word: str) -> bool:
        wordExists = False
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == word[0]:
                    # store the chrInd (equivalent to the depth of the search)
                    visitedMatrix = [[-1 for _ in range(len(board[0]))] for _ in range(len(board))]
                    startCoord = (y,x)
                    print("*** startCoord: ", startCoord)
                    wordExists = wordExists | self.dfs(board, word, startCoord, 0, visitedMatrix)
                    if wordExists == True:
                        return wordExists
        return wordExists

    def dfs(self, board, word, currCoord, chrInd, visitedMatrix):
        #print("----------------")
        if chrInd >= len(word):
            #print("charind is equal to len: ", chrInd)
            #print("currCoord is : ", currCoord)
            if board[currCoord[0]][currCoord[1]] == word[-1]:
                return True
            else:
                return False

        if board[currCoord[0]][currCoord[1]] != word[chrInd]:
            return False

        #print("currCoord: {}, chrInd: {}".format(currCoord, chrInd))
        visitedMatrix[currCoord[0]][currCoord[1]] = chrInd
        #for row in visitedMatrix: print(" {}".format(row))

        # find next valid moves
        if chrInd < len(word)-1:
            availMoves = self.nextMoves(board, word, currCoord, chrInd+1)
            #print("availMoves: ", availMoves)
            result = False
            for move in availMoves:
                y = move[0]; x = move[1]
                if visitedMatrix[y][x] == -1:
                    #print("calling dfs for move: {}, chrInd: {}".format(move, chrInd+1))
                    result = result | self.dfs(board, word, move, chrInd+1, visitedMatrix)
                    # this is needed to allow the dfs to explore more than 1 path with the same subsequence until some mismatch.s
                    visitedMatrix[y][x] = -1 
            return result
        
        return self.dfs(board, word, currCoord, chrInd+1, visitedMatrix)

    def nextMoves(self, board, word, fromCoord, chrInd):
        moveCoords = [] # tuples (y,x)
        yMax = len(board)-1
        xMax = len(board[0])-1
        yc = fromCoord[0]
        xc = fromCoord[1]
        if yc > 0 and board[yc-1][xc]==word[chrInd]:
            moveCoords.append((yc-1, xc))
        if yc < yMax and board[yc+1][xc]==word[chrInd]:
            moveCoords.append((yc+1, xc))
        if xc > 0 and board[yc][xc-1]==word[chrInd]:
            moveCoords.append((yc, xc-1))
        if xc < xMax and board[yc][xc+1]==word[chrInd]:
            moveCoords.append((yc, xc+1))

        return moveCoords

    def test1(self):
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]
        #word = "ABCCED"
        word = "SEE"
        #word = "ABCB"
        #word = "ABCCEDASF"
        #word = "ABCCEDASFC"
        res = self.exist(board, word)
        print("test1 res: ", res)

    def test2(self):
        board =[["C","A","A"],
                ["A","A","A"],
                ["B","C","D"]]
        #word = "AAB" # expected True
        word = "AABB"
        res = self.exist(board, word)
        print("test2 res: ", res)

    def test3(self):
        board = [["a"]]
        word = "b"
        res = self.exist(board, word)
        print("test3 res: ", res)

    def test4(self):
        board = [["A","B","C","E"],
                ["S","F","E","S"],
                ["A","D","E","E"]]
        word = "ABCESEEEFS" # expected: True
        res = self.exist(board, word)
        print("test4 res: ", res)

    def test5(self):
        board =[["F","Y","C","E","N","R","D"],
                ["K","L","N","F","I","N","U"],
                ["A","A","A","R","A","H","R"],
                ["N","D","K","L","P","N","E"],
                ["A","L","A","N","S","A","P"],
                ["O","O","G","O","T","P","N"],
                ["H","P","O","L","A","N","O"]]
        #word = "USA" # expected False
        #word = "NARAHNA"
        word = "ASDF"
        res = self.exist(board, word)
        print("test5 res: ", res)

    def test6(self):
        board =[["a"]*30] * 29
        board.append(["a"]*29 + ["b"])
        
        for row in board:
            print(" ", row)

        word = "baaaaaaaaaaaaaaa" # True
        #word = "caaaaaaaaaaaaaaaa" # False
        res = self.exist(board, word)
        print("test6 res: ", res)

s = Solution()
#s.test1()
#s.test2()
#s.test3()
#s.test4()
#s.test5()
s.test6()