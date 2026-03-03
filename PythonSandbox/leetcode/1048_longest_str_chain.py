# https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: [str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        #print("words sorted by len:\n", words)
        dp = [1 for _ in range(len(words))]
        #print("dp: ", dp)
        ans = 0
        for i in range(len(words)):
            for j in range(i):
                word1 = words[i]; word2 = words[j]
                #print("i={}, j={}, word1:{}, word2:{}".format(i,j,word1,word2))
                wordsAreChain = self.isChain(word1, word2)
                if wordsAreChain:
                    #print(" wordsAreChain: ", wordsAreChain)
                    dp[i] = max(dp[i], dp[j]+1)
                #print(" dp: ", dp)
                ans = max(ans, dp[i])
        #print("dp final: ", dp)
        return ans
    
    def isChain(self, word1, word2):
        i = 0
        j = 0
        if abs(len(word1)-len(word2)) > 1 or abs(len(word1)-len(word2))==0:
            return False
        diffs = 0
        while i < len(word1) and j < len(word2):
            if word1[i]==word2[j]:
                i += 1
                j += 1
            elif word1[i]!=word2[j] and diffs==0: # only allow 1 diff
                i += 1
                diffs += 1 
            else:
                return False
        
        return True