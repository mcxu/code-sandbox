'''
https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.helper(s, 0, memo)
    
    def helper(self, s, i, memo):
        if i < len(s) and s[i] == "0":
            return 0
        if i >= len(s)-1:
            return 1 # return 1 for 1 successful path
        
        if i in memo.keys():
            return memo[i]
        
        nways = self.helper(s, i+1, memo)
        if int(s[i:i+2]) <= 26:
            nways += self.helper(s, i+2, memo)
        
        memo[i] = nways
        return memo[i]