'''
https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''

class Solution:
    # recursive, with memoization
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        wordDict = set(wordDict)
        i = 0
        memo = [None for _ in range(len(s)+1)]
        return self.helper(s, wordDict, i, memo)
    
    def helper(self, s, wordDict, i, memo):
        #print("starting i= ", i)
        if i >= len(s):
            return True
        
        if memo[i] != None:
            return memo[i]
        
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            subResult = self.helper(s, wordDict, j, memo)
            if substr in wordDict and subResult==True:
                memo[i] = True
                return memo[i]
        
        memo[i] = False
        return memo[i]