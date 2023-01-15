'''
LC221 https://leetcode.com/problems/maximal-square/
'''
class Solution:
    '''
    DP, best space complexity
    Time: O(n*m), n = matrix vertical length, m = matrix horizontal length
    Space: O(m), since aux is the width of the matrix, but only 2 rows of depth is needed.
    '''
    def maximalSquare2(self, matrix: [[str]]) -> int:
        if not matrix:
            return 0
        
        # turn into numbers
        for i in range(len(matrix)):
            matrix[i] = [int(x) for x in matrix[i]]
            
        aux = [[0 for _ in range(len(matrix[0])+1)] for _ in range(2)]
        
        maxSideSoFar = 0
        for y in range(1, len(matrix)+1):
            for x in range(1, len(aux[0])):
                if matrix[y-1][x-1] == 1:
                    aux[1][x] = min(aux[0][x],
                                    aux[1][x-1],
                                    aux[0][x-1])+1 
                    if aux[1][x] > maxSideSoFar:
                        maxSideSoFar = aux[1][x]

            # shift aux down; which means shifting bottom row of aux up.
            aux[0] = aux[1]
            aux[1] = [0 for _ in range(len(aux[0]))]
            
        return maxSideSoFar**2

    # ======================================================================
    # DP Solution but not the one with the least space complexity.
    def maximalSquare(self, matrix: [[str]]) -> int:
        if not matrix:
            return 0
        
        # turn into numbers
        for i in range(len(matrix)):
            matrix[i] = [int(x) for x in matrix[i]]

        aux = [[0 for _ in range(len(matrix[0])+1)] 
                for _ in range(len(matrix)+1)]
        
        maxSideSoFar = 0
        for y in range(1, len(aux)):
            for x in range(1, len(aux[y])):
                if matrix[y-1][x-1] == 1:
                    aux[y][x] = min(aux[y-1][x],
                                    aux[y][x-1],
                                    aux[y-1][x-1])+1 
                    if aux[y][x] > maxSideSoFar:
                        maxSideSoFar = aux[y][x]

        return maxSideSoFar**2