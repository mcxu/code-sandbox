"""
https://www.facebook.com/careers/life/sample_interview_questions

Spiral Array:

input = 3
123
894
765

input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

input = 8
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
"""

class Prob:
    @staticmethod
    def getSpiralMatrix(input):
        matrix = [[0 for x in range(input)] for y in range(input)]
        print("matrix: ", matrix)
        
        # limits
        maxVal = input**2 # maximum value to count up to
        yindMin = 0
        xindMin = 0
        yindMax = len(matrix)-1;
        xindMax = len(matrix[0])-1;
        print("maxVal: %s, yindMax: %s, xindMax: %s" % (maxVal, yindMax, xindMax))
        
        # starting numbers
        currVal = 1 # starting value from cell (0,0)
        
        while(currVal <= maxVal):
            # move right 
            print("moving right")
            for i in range(xindMin, xindMax+1):
                print("    move right: i(xind): %s, currVal: %s" % (i,currVal))
                matrix[yindMin][i] = currVal
                currVal += 1
            
            print("matrix after move right:", matrix)
            yindMin += 1
            
            # move down
            print("moving down")
            for i in range(yindMin, yindMax+1):
                print("    move down: i(yind): %s, currVal: %s" % (i,currVal))
                matrix[i][xindMax] = currVal
                currVal += 1
            
            print("matrix after move down:", matrix)
            xindMax -= 1
            
            # move left
            print("moving left")
            for i in range(xindMax, xindMin-1, -1):
                print("    move left: i(xind): %s, currVal: %s" % (i,currVal))
                matrix[yindMax][i] = currVal
                currVal += 1
                
            print("matrix after move left: ", matrix)
            yindMax -= 1
            
            # move up
            print("moving up")
            for i in range(yindMax, yindMin-1, -1):
                print("    move up: i(yind): %s, currVal: %s" % (i,currVal))
                matrix[i][xindMin] = currVal
                currVal += 1
            
            print("matrix after move up: ", matrix)
            xindMin += 1
            
        return matrix

    @staticmethod
    def printMatrix(matrix):
        for ylist in matrix:
            print(ylist)

    @staticmethod
    def testInitMatrix():
        input = 4
        spiralMatrix = [[0 for i in range(input)] for j in range(input)]
        print("testInitMatrix: ", spiralMatrix)
    
    @staticmethod
    def test1():
        input = 4
        m = Prob.getSpiralMatrix(input)
        Prob.printMatrix(m)

#Prob.testInitMatrix()
Prob.test1()
