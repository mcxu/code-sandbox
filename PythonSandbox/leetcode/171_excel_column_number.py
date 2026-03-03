'''
https://leetcode.com/problems/excel-sheet-column-number/
'''
import string

class Solution:
    def titleToNumber(self, s: str) -> int:
        chMap = {}
        for i,ch in enumerate(string.ascii_uppercase):
            chMap[ch] = i+1
        
        n = 0
        for i in range(len(s)):
            ch = s[len(s)-1-i]
            #print("ch: ", ch)
            n += (chMap[ch] * (26**i))
        return n
            