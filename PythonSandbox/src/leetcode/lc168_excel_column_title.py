'''
https://leetcode.com/problems/excel-sheet-column-title/
'''
import string 

class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ""
        while n > 0:
            #print("n: ", n)
            mod = int(n%26)
            if mod > 0:
                title += string.ascii_uppercase[mod-1]
                n -= mod
            else:
                title += "Z"
                n -= 1
            n = int(n/26)
        
        #print("title: ", title)
        return title[::-1]