#https://leetcode.com/problems/longest-common-prefix/

class Solution2:
    # Using trie.
    def longestCommonPrefix(self, strs: [str]) -> str:
        trieRoot, shortestStrLen = self.buildTrie(strs)
        
        # build the shortest prefix  
        ptr = trieRoot
        builtPrefix = ""
        while len(ptr.keys()) == 1 and len(builtPrefix) < shortestStrLen:
            currKey = list(ptr.keys())[0]
            builtPrefix += currKey
            ptr = ptr[currKey]
        
        return builtPrefix
                    
                        
    def buildTrie(self, strs, shortestStrLen = float('inf')):
        trieRoot = {}

        for string in strs:
            
            if string == "":
                return {}, 0
            else:
                shortestStrLen = min(shortestStrLen, len(string))

            ptr = trieRoot
            for char in string:
                if char not in ptr.keys():
                    ptr[char] = {}
                ptr = ptr[char]

        return trieRoot, shortestStrLen
    
    # ========== test ==========

    def doDFS(self, trieRoot, currPath: str, allPaths: set):
        if trieRoot == None:
            return trieRoot
        
        if not trieRoot:
            allPaths.add(currPath)
            return

        for child in trieRoot.keys():
            self.doDFS(trieRoot[child], currPath+child, allPaths)

    def test(self):
        cases = [
            dict(strs= ["flower","flow","flight"], output= "fl"),
            dict(strs= ["dog","racecar","car"], output = ""),
            dict(strs = ["ab", "a"], output = "a")
        ]

        for c in cases:
            res = self.longestCommonPrefix(c["strs"])
            print("case: ", c)
            print("res: ", res)
            assert res == c["output"]

    # ==========================================================

class Solution:
    def longestCommonPrefix_1stAttempt(self, strs: [str]) -> str:
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

sol = Solution2()
sol.test()