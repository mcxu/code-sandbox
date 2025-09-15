'''
Function to determine if a substring k exists in a string s.
If k exists in s, return the index of the char in s that k starts.
If k doesn't exist inside of s, return -1. 
Note: implement from scratch, cannot use built in substring function.
'''
import time
class Solution:
    # O(len(s)) time, O(1) space
    def substr(self, s, k):
        i = 0; j = 0
        m = False # stores whether there was a previous match
        while i < len(s) and j < len(k):
            if s[i] == k[j]:
                j += 1
                m = True
            else:
                if m:
                    j = 0
                    i -= 1
                    m = False
            i += 1
            
        if j >= len(k):
            return i-len(k)
        return -1
    
    def test1(self):
        s = "hellothere"
        k = "other"
        res = self.substr(s, k)
        print("res: ", res)

    def test2(self):
        s = "hellothere"
        k = "hella"
        res = self.substr(s, k)
        print("res: ", res)

s = Solution()
s.test1()
#s.test2()
    

        
