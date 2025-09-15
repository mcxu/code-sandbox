""" 
https://leetcode.com/problems/longest-palindromic-substring/description/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps = ""
        for i,c in enumerate(s):
            # expand for i (odd)
            [startIdxOdd, endIdxOdd] = self.expand(i, i, s)
            # exapand for i+1 (even)
            [startIdxEven, endIdxEven] = self.expand(i, i+1, s)
            
            if endIdxEven-startIdxEven > len(lps):
                lps = s[startIdxEven: endIdxEven]
            elif endIdxOdd-startIdxOdd > len(lps):
                lps = s[startIdxOdd: endIdxOdd]

        return lps

    def expand(self, i, j, s):
        while i >= 0 and j < len(s) and s[i]==s[j]:
            i -= 1
            j += 1

    def expand(self, i, j, s):
        while i >= 0 and j < len(s) and s[i]==s[j]:
            i -= 1
            j += 1

        return [i+1, j]
    
    def test1(self):
        #s = "babad"
        s = "cbbd"
        res = self.longestPalindrome(s)
        print("res: ", res)
    
c = Solution()
c.test1()
    