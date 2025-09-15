'''
https://leetcode.com/problems/spiral-matrix/
'''

class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return matrix
        if not matrix[0]:
            return matrix[0]
        
        yMin=0
        yMax=len(matrix)-1
        xMin=0
        xMax=len(matrix[0])-1
        c = 0
        tot = len(matrix) * len(matrix[0])
        out = []
        while c < tot:
            for i in range(xMin, xMax+1):
                out.append(matrix[yMin][i])
                c+=1
            yMin += 1
            if c==tot: return out
            
            for i in range(yMin, yMax+1):
                out.append(matrix[i][xMax])
                c+=1
            xMax -= 1
            if c==tot: return out
            
            for i in range(xMax, xMin-1, -1):
                out.append(matrix[yMax][i])
                c+=1
            yMax -= 1
            if c==tot: return out
            
            for i in range(yMax, yMin-1, -1):
                out.append(matrix[i][xMin])
                c+=1
            xMin += 1
            if c==tot: return out
            
        return out