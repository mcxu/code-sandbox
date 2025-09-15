class Solution:
    def lcp_2_arrays(self, words1, words2):
        trie1 = self.buildTrie(words1)
        
        matchingPrefixes = []
        for word in words2:
            #dfs
            i = 0
            currPrefix = ""
            self.dfs(trie1, word, i, currPrefix, matchingPrefixes)
        
        longestPrefix = ""
        for p in matchingPrefixes:
            if len(p) > len(longestPrefix):
                longestPrefix = p
        return longestPrefix


    def dfs(self, trie, word, i, currPrefix, matchingPrefixes):
        if trie == None or trie == {}:
            matchingPrefixes.append(currPrefix)
            return

        if i >= len(word):
            matchingPrefixes.append(currPrefix)
            return

        if word[i] not in trie.keys():
            matchingPrefixes.append(currPrefix)
            return
        
        for k in trie.keys():
            self.dfs(trie[k], word, i+1, currPrefix+word[i], matchingPrefixes)

    def buildTrie(self, arr):
        trie = {}
        for word in arr:
            n = trie
            for ch in word:
                if ch not in n.keys():
                    n[ch] = {}
                n = n[ch]
        return trie

    def test(self):
        words1 = ["a", "bc", "def", "asdfg", "dfghdfgh"]
        words2 = ["q", "qwerty", "asdf", "dfga"]
        longestPrefix = self.lcp_2_arrays(words1, words2)
        print("longestPrefix: ", longestPrefix)

sol = Solution()
sol.test()