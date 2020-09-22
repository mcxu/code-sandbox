'''
https://leetcode.com/problems/consecutive-characters/
'''

class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        j = 0
        mp = 0
        while i < len(s):
            if s[j]!=s[i]:
                j = i
            mp = max(mp, i-j+1)
            i += 1
        return mp