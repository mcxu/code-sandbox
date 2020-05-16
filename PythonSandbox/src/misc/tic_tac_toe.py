'''
Simple game of tic tac toe
'''
class TicTacToe:
    def __init__(self):
        self.p1 = "Player 1"
        self.p2 = "Player 2"
        self.pMap = {self.p1:"X", self.p2:"O"}
        self.grid = [[None for _ in range(3)] for _ in range(3)]
        self.LIM = 3
        print("TicTacToe: player 1: {}, player 2: {}".format(self.pMap[self.p1], self.pMap[self.p2]))
    
    def getGridState(self):
        return self.grid
    
    # returns true if updated, returns false if not updated 
    # (probably due to the cell already being occupied)
    def updateGrid(self, player, y, x):
        if self.grid[y][x] != None:
            return False
        self.grid[y][x] = self.pMap[player]
        return True

    # does a player have 3 of their symbols in a row?
    def detect3InARow(self, player):
        symbol = self.pMap[player]

        # see if rows contain 3 in a row.
        for y in range(len(self.grid)):
            count = 0
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == symbol:
                    count +=1
            if count == self.LIM:
                return True
        
        # see if cols contain 3 in row.
        for x in range(len(self.grid[0])):
            count = 0
            for y in range(len(self.grid)):
                if self.grid[y][x] == symbol:
                    count += 1
            if count == self.LIM:
                return True
        
        # check diagonals
        count = 0
        for y in range(len(self.grid)):
            if self.grid[y][y] == symbol:
                count += 1
        if count == self.LIM:
            return True
        
        count = 0
        x = 0
        for y in range(len(self.grid)-1, -1, -1):
            if self.grid[y][x] == symbol:
                count += 1
            x += 1
        if count == self.LIM:
            return True
        
        return False
    
    def isGridAllFilled(self):
        LIM = 9
        count = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != None:
                    count += 1
        if count < LIM:
            return False
        return True

class Driver:
    def __init__(self):
        self.ttt = TicTacToe()

    # error checking for user inputs
    # returns [inputGood, y, x]
    def inputCheck(self, inputCoord):
        inputSplit = inputCoord.split(",")
        if len(inputSplit) < 2:
            return [False, None, None]
        y = int(inputSplit[0])
        x = int(inputSplit[1])
        if 0 <= y <= 2 and 0 <= x <= 2:
            return [True, y, x]
        else:
            return [False, None, None]

    def runGame(self):
        try:
            currPlayer = self.ttt.p1
            print("currPlayer:", currPlayer)
            exists3InRow = self.ttt.detect3InARow(currPlayer)
            gridAllFilled = self.ttt.isGridAllFilled()
            y,x = None, None
            while exists3InRow == False and not gridAllFilled:
                print("{} input a coordinate in the format: y,x".format(currPlayer)),
                inputCoord = input()
                inputGood = self.inputCheck(inputCoord)
                if inputGood[0]:
                    y = inputGood[1]
                    x = inputGood[2]
                else:
                    continue

                updateStatus = self.ttt.updateGrid(currPlayer, y, x)
                if updateStatus:
                    print("grid has been updated to:")
                    for row in self.ttt.grid:
                        print(" ", row)

                    exists3InRow = self.ttt.detect3InARow(currPlayer)
                    gridAllFilled = self.ttt.isGridAllFilled()

                    if gridAllFilled == True:
                        break

                    # switch players:
                    if currPlayer == self.ttt.p1:
                        currPlayer = self.ttt.p2
                    else:
                        currPlayer = self.ttt.p1
                else:
                    print("     !!! Hey {}, that cell has already been filled.".format(currPlayer))
            
            if exists3InRow == True:    
                print("{} has won.".format(currPlayer))
            elif gridAllFilled == True:
                print("The game is a draw.")

            print("game grid final: ")
            for row in self.ttt.grid: print(" ", row)

        except KeyboardInterrupt:
            print("Game stopped, grid state:")
            for row in self.ttt.grid: print(" ", row)

driver = Driver()
driver.runGame()
