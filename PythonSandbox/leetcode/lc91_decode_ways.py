'''
https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0 for _ in range(len(s))]
        return self.dfs(s, 0, memo)

    def dfs(self, s, i, memo):
        if i <= len(s)-1 and s[i] == "0":
            return 0

        if i >= len(s)-1:
            # return 1 for 1 successful path
            # e.g. if s = "3", then idx 0 is at the end, but 3 is a valid number so that is 1 decoded string
            return 1 

        if memo[i] != 0:
            return memo[i]

        numWays = self.dfs(s, i+1, memo)
        if int(s[i:i+2]) <= 26:
            numWays += self.dfs(s, i+2, memo)

        memo[i] = numWays
        return numWays