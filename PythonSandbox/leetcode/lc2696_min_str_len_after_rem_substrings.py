"""
https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
"""

class Solution:
    def minLength(self, s: str) -> int:
        
        while "AB" in s or "CD" in s:
            # print("s: ", s)
            sList = list(s)
            if "AB" in s:
                idx = s.index("AB")
                sList.pop(idx)
                sList.pop(idx)
            elif "CD" in s:
                idx = s.index("CD")
                sList.pop(idx)
                sList.pop(idx)
            
            # print("sList: ", sList)
            
            newS = "".join(sList)
            s = newS
        
        return len(s)