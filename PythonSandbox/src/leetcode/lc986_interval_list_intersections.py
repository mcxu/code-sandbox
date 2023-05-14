'''
https://leetcode.com/problems/interval-list-intersections/
'''

class Solution:
    def intervalIntersection(self, A, B):
        out = []
        i = 0
        j= 0
        while i<len(A) and j<len(B):
            aInt = A[i]
            bInt = B[j]
            
            intersection = []
            
            # find start of intersection
            if aInt[0] <= bInt[0]:
                intersection.append(bInt[0])
            else:
                intersection.append(aInt[0])
            # find end of intersection
            if aInt[1] >= bInt[1]:
                intersection.append(bInt[1])
            else:
                intersection.append(aInt[1])
            # check if intersection is valid
            if intersection[0] <= intersection[1]:
                out.append(intersection)
            # increment pointer of which ending is lower
            if aInt[1] < bInt[1]:
                i += 1
            else:
                j += 1
            
        return out