'''
Rotate Matrix

Given 2-d array (matrix), write 1 function to rotate it 
90 degrees Clockwise, and Counterclockwise.

https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
https://www.youtube.com/watch?v=IdZlsG6P17w
'''

import copy

class Prob:
    @staticmethod
    def rotateMatrix(mtx, cw=True):
        # transpose
        mtxT = Prob.transpose(mtx)
        
        try:
            if cw == True:
                for row in mtxT:
                    row = Prob.reverseRow(row)
            elif cw == False:
                medianColInd = int(len(mtxT)/2)
                for x in range(len(mtxT[0])):
                    for y in range(medianColInd):
                        tmp = mtxT[y][x]
                        mtxT[y][x] = mtxT[len(mtx)-1-y][x]
                        mtxT[len(mtxT)-1-y][x] = tmp
            else:
                raise ValueError("param cw must either be True or False (ccw)")
        except ValueError as err:
            print(err)
        
        return mtx
    
    @staticmethod
    def transpose(mtx):
        for y in range(len(mtx)):
            for x in range(y):
                tmp = mtx[y][x]
                mtx[y][x] = mtx[x][y]
                mtx[x][y] = tmp
        
        return mtx
    
    @staticmethod
    def reverseRow(array):
        medianInd = int(len(array)/2)
        for i in range(medianInd):
            tmp  = array[i]
            array[i] = array[len(array)-1-i]
            array[len(array)-1-i] = tmp
        return array
        
    
    @staticmethod
    def test_transpose():
        mtx = [ [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10,11,12],
                [13,14,15,16]]
        
        mtxT = Prob.transpose(mtx)
        print("test_transpose mtxT: ", mtxT)
    
    @staticmethod
    def test_reverseRow():
        array = [1,2,3,4,5,6,7,8,9]
        rev = Prob.reverseRow(array)
        print("rev: ", rev)
    
    @staticmethod
    def test1():
        mtx = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    
        mtxCopy = copy.deepcopy(mtx)
        print("mtxCopy: ", mtxCopy)
        
        mtxRCW = Prob.rotateMatrix(mtx, cw=True)
        print("test1 mtxRCW: ", mtxRCW)
        mtxRCCW = Prob.rotateMatrix(mtxCopy, cw=False)
        print("test1 mtxRCCW: ", mtxRCCW)
    
    @staticmethod
    def test2():
        mtx = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10,11,12],
               [13,14,15,16]]
        
        mtxCopy = copy.deepcopy(mtx)
        
        mtxRCW = Prob.rotateMatrix(mtx, cw=True)
        print("test2 mtxRCW: ", mtxRCW)
        mtxRCCW = Prob.rotateMatrix(mtxCopy, cw=False)
        print("test2 mtxRCCW: ", mtxRCCW)
        
#Prob.test_reverseRow()   
#Prob.test1()
Prob.test2()


