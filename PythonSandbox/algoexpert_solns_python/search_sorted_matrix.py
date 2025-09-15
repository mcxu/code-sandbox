'''
Search in sorted matrix
Given 2d-array where rows and columns are sorted, find the row and column indices of a target value to search.
IF searched value is not in matrix, return [-1,-1]

Sample input: matrix1(), target: 44
Sample output: [3,3]
'''

class Prob:
    
    """
    Time complexity: O(rows + columns)
    Space complexity: O(1), since only the current index and value is stored each recursion
    """
    @staticmethod
    def searchInSortedMatrix(matrix, target):
        rowInd = 0
        colInd = len(matrix[0])-1
        rowIndMax = len(matrix)-1
        colIndMin = 0
        
        while rowInd <= rowIndMax and colInd >= colIndMin:
            currInd = [rowInd, colInd]
            currVal = matrix[rowInd][colInd]
            print("currInd: {}, currVal: {}".format(currInd, currVal))
            
            if currVal == target:
                return currInd
            
            if currVal > target:
                print("    colInd-1")
                colInd -= 1
            
            if currVal < target:
                print("    rowInd+1")
                rowInd += 1
        
        return [-1, -1]
            
    @staticmethod
    def matrix1():
        m = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
            ]
        return m
    
    @staticmethod
    def test1():
        m = Prob.matrix1()
        targetInd = Prob.searchInSortedMatrix(m, 98)
        print("test1: targetInd: ", targetInd)

Prob.test1()
