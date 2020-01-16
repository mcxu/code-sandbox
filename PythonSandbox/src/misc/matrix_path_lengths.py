'''
Paths of adjacent particular value in matrix.
Given matrix (2d array) of 0's and 1's, return an array of the lengths of the paths of all 1's. 
Left/right and up/down are valid routes, but diagonals are not.

Sample input:
[[1,0,0,1,0],
 [1,0,1,0,0],
 [0,0,1,0,1],
 [1,0,1,0,1],
 [1,0,1,1,0]]

Sample output: [1,2,2,2,5]
'''
import time
   
class Prob:
    @staticmethod
    def getLengths(matrix):
        # array to store found paths
        paths = []
        
        # auxilary matrix to store visited state (False: unvisited, True: visited)
        aux = [[False for i in row] for row in matrix]
        print("aux: ", aux)
        
        # populate aux with QItem objects instead of just values.
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                #print("i={}, j={}".format(i,j))
                val = matrix[j][i]
                print("i={}, j={}, val = {}".format(i, j, val))
                
                visitedState = aux[j][i]
                print("    visitedState: ", visitedState)
                
                if visitedState == False:
                    Prob.doBfs(j, i, matrix, aux, paths)
        
        print("!!!! paths: ", paths)
                        
                        
    @staticmethod
    def doBfs(j, i, matrix, aux, paths):
        queue = [[j,i]]
        pathLength = 0
        while(queue):
            currCoord = queue.pop(0) # pop first
            print("    --- currCoord: ", currCoord)
            currj = currCoord[0]
            curri = currCoord[1]
            
            # check if currCoord has been visited
            visitedState = aux[currj][curri]
            print("    currCoord has been visited: ", visitedState)
#             if visitedState:
#                 continue
            
            # label currCoord as visited
            aux[currj][curri] = True
            print("    aux now: ", aux)
            
            currVal = matrix[currj][curri]
            print("    currVal: ", currVal)
            if currVal >= 1:
                pathLength += currVal
            else:
                continue
            
            # search neighbors
            unvisiteds = Prob.getUnvisitedNeighbors(currj, curri, matrix, aux)
            queue += unvisiteds
            print("    queue: ", queue)
            time.sleep(.5)
        paths.append(pathLength)
            
    @staticmethod
    def getUnvisitedNeighbors(j, i, matrix, aux):
        print("        getUnvisitedNeighbors: j={}, i={}".format(j,i))
        unvisiteds = [] # unvisited neighbors (j,i) from a chosen (j,i)
        
        # check above
        if j > 0 and aux[j-1][i] == False:
            unvisiteds.append([j-1,i])
        
        # check below
        if j < (len(matrix)-1) and aux[j+1][i] == False:
            unvisiteds.append([j+1,i])
        
        # check left
        if i > 0 and aux[j][i-1] == False:
            unvisiteds.append([j,i-1])
        
        # check right
        if i < (len(matrix)-1) and aux[j][i+1] == False:
            unvisiteds.append([j,i+1])
        
        print("        univisiteds: ", unvisiteds)
        return unvisiteds
        
    @staticmethod
    def test_doBfs():
        matrix = [
            [1,0,0,1,0],
            [1,0,1,0,0],
            [0,0,1,0,1],
            [1,0,1,0,1],
            [1,0,1,1,0]]
        # array to store found paths
        paths = []
        
        # auxilary matrix to store visited state (False: unvisited, True: visited)
        aux = [[False for i in row] for row in matrix]
        print("aux: ", aux)
        j=1
        i=2
        Prob.doBfs(j, i, matrix, aux, paths)
        print("paths is now: ", paths)
    
    @staticmethod
    def test1():
        matrix = [
            [1,0,0,1,0],
            [1,0,1,0,0],
            [0,0,1,0,1],
            [1,0,1,0,1],
            [1,0,1,1,0]]
        Prob.getLengths(matrix)

#Prob.test1()
Prob.test_doBfs()           
        
        