'''
https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''
class Solution:
    # recursive, with memoization
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        wd = set(wordDict)
        memo = {}
        return self.subStrIsSegment(s, wd, 0, memo)
    
    # are there any substring in s that are in wordDict?
    def subStrIsSegment(self, s, wd, i, memo): # i=beginning index of substr
        
        if i >= len(s):
            return True

        if i in memo:
            return memo[i]

        for j in range(i+1, len(s)+1):
            subStr = s[i:j]
            restOfStrIsSegment = self.subStrIsSegment(s, wd, j, memo) # is the rest of the string also in word dict?
            if subStr in wd and restOfStrIsSegment: # in current substring in worddict AND rest of the string in word dict?
                memo[i] = True
                return True

        memo[i] = False
        return False
    
    def test(self):
        cases = [
            # dict(s="leetcode", wordDict=["leet","code"], expected=True),
            # dict(s="a", wordDict=["a"], expected=True),
            dict(s="applepenapple", wordDict=["apple","pen"], expected=True)
        ]

        for case in cases:
            print("case: ", case)
            res = self.wordBreak(case["s"], case["wordDict"])
            print("res: ", res)
            assert res == case["expected"]
    
    # recursive, without memoization
    def wordBreak_noMemo(self, s: str, wordDict: [str]) -> bool:
        wd = set(wordDict)

    def subStrIsSegment(self, s, wd, i):
        if i >= len(s):
            return True
        
        for j in range(i+1, len(s)+1):
            subStr = s[i:j]
            restOfStrIsSegment = self.subStrIsSegment(s, wd, j)
            if subStr in wd and restOfStrIsSegment:
                return True
        
        return False

sol = Solution()
sol.test()