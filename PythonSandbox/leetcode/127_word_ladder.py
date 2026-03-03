# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength2(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        comboMap = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i]+"*"+word[i+1:]
                if s in comboMap.keys():
                    comboMap[s].append(word)
                else:
                    comboMap[s] = [word] 
                    
        q = [(beginWord,1)]
        visited = set(beginWord)
        while q:
            currWordTup = q.pop(0)
            currWord = currWordTup[0]
            currLevel = currWordTup[1]
            
            for i in range(len(currWord)):
                tmpWord = currWord[:i]+"*"+currWord[i+1:]
                if tmpWord in comboMap.keys():
                    for word in comboMap[tmpWord]:
                        if word == endWord:
                            return currLevel+1
                        if word not in visited:
                            visited.add(word)
                            q.append((word, currLevel+1))
                        
        return 0

    # ============================================================
    # TLE

    def ladderLength1(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        
        q = [(beginWord,1)]
        visited = set([beginWord])
        while q:
            currWordTup = q.pop(0)
            currWord = currWordTup[0]
            currLevel = currWordTup[1]
            
            i = 0
            while i < len(wordList):
                word = wordList[i]
                if self.countDiffs(word, currWord)==1:
                    if word == endWord:
                        return currLevel+1
                    
                    if word not in visited:
                        visited.add(word)
                        q.append((word, currLevel+1))
                        wordList.pop(i)
                        i -= 1
                i += 1
                
        return 0
    
    def countDiffs(self, word1, word2):
        c = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                c += 1
        return c