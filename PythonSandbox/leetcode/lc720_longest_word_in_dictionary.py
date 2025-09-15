# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: [str]) -> str:
        wordsSet = set(words)
        #print("wordsSet: ", wordsSet)
        trie = {}
        for i,word in enumerate(words):
            n = trie
            j = 0
            while j < len(word):
                ch = word[j]
                if ch not in n.keys():
                    n[ch] = {}
                n = n[ch]
                j += 1
        #print("trie: ", trie)
        
        # search trie
        solutions=set()
        builtStr = ""
        self.dfs(trie, builtStr, solutions, wordsSet)
        #print("solutions after dfs:", solutions)
        
        lenmap= {}
        for s in solutions:
            if len(s) in lenmap:
                lenmap[len(s)].append(s)
            else:
                lenmap[len(s)]=[s]
        
        longestWords = lenmap[max(lenmap.keys())]
        longestWordsLex = sorted(longestWords)
        return longestWordsLex[0]
        
    
    def dfs(self, n, builtStr, solutions, wordsSet):
        if n == {}:
            if builtStr not in solutions:
                solutions.add(builtStr)
            return
        
        # if builtStr is not in the wordsSet, then builtStr without its last char
        # must have been part of the wordsSet.
        if builtStr and builtStr not in wordsSet:
            prevSubstring = builtStr[:-1]
            if prevSubstring:
                solutions.add(prevSubstring)
            return
        
        for k in n.keys():
            self.dfs(n[k], builtStr+k, solutions, wordsSet)
        