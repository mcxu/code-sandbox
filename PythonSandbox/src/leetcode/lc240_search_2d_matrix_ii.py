# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                targetExists = self.binarySearchArr(row, target)
                if targetExists:
                    return True
        return False
        
    
    def binarySearchArr(self, arr, target):
        i = 0
        j = len(arr)-1
        while i <=  j:
            med = int((i + j)/2)
            num = arr[med]
            if num == target:
                return True
        
            if num < target:
                i = med+1
            elif num > target:
                j = med-1
            
        return False