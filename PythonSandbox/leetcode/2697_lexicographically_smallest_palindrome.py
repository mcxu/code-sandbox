"""
https://leetcode.com/problems/lexicographically-smallest-palindrome/description/
"""

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        swapIndices = []
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                swapIndices.append(i)
        
        sList = list(s)
        for i in swapIndices:
            if sList[i] < sList[-1-i]:
                sList[-1-i] = sList[i]
            elif sList[i] > sList[-1-i]:
                sList[i] = sList[-1-i]

        return "".join(sList)
    