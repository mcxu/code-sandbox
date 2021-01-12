#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    # Using trie.
    def longestCommonPrefix2(self, strs: [str]) -> str:
        trie, shortest = self.buildTrie(strs)
        
        # traverse the trie to build the common prefix
        n = trie
        commonPref = ""
        while len(n.keys())==1 and shortest>0:
            k = list(n.keys())[0]
            commonPref += k
            n = n[k]
            shortest -= 1
        return commonPref
    
    def buildTrie(self, strs):
        trie = {}
        shortest = float('inf') # length of the shortest word
        for i,word in enumerate(strs):
            if len(word) < shortest:
                shortest = len(word)
            
            n = trie
            if word:  
                for j,ch in enumerate(word):
                    if ch not in n.keys():
                        n[ch] = {}
                    n = n[ch]
            else:
                n[word] = {}
                
        return trie, shortest

    # ==========================================================

    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
        
        i = 0
        j = 0
        
        if not (strs[i] and len(strs[i]) > 0):
            return ""            
        
        refChar = strs[i][j]
        commonPref = ""
        while i < len(strs):
            word = strs[i]
            
            if j > len(word)-1:
                return commonPref
            
            currChar = word[j]
            if currChar != refChar:
                return commonPref
            
            i += 1
            if i > len(strs)-1:
                commonPref += word[j]
                i = 0
                word = strs[i]
                j += 1
                if j > len(word)-1:
                    return commonPref
                refChar = word[j]
                
        return commonPref