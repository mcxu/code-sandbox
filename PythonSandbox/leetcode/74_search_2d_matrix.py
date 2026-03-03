'''
https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        rowInd = len(matrix)-1
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                rowInd = i
                break
        
        return self.binarySearch(matrix[rowInd], target)
        
    def binarySearch(self, row, target):
        i = 0
        j = len(row)-1
        while i <= j:
            med = int((i+j)/2)
            
            if row[med] == target:
                return True
            
            if row[med] > target:
                j = med-1
            elif row[med] < target:
                i = med+1
        
        return False