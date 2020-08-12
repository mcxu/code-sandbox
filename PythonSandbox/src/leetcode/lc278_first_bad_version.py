'''
https://leetcode.com/problems/first-bad-version/
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        m = int((j+i)/2)
        isBad = isBadVersion(m)
        while i < j:
            if isBadVersion(m-1)==False and isBadVersion(m)==True:
                return m
            
            if isBad==False: # check right
                i = m+1
            else:
                j = m-1
            m = int((j+i)/2)
            isBad = isBadVersion(m)
        return m
    
