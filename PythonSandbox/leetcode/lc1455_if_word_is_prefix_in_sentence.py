'''
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
'''
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentSplit = sentence.split(" ")
        for i,word in enumerate(sentSplit):
            if self.isPrefix(searchWord, word):
                return i+1
        return -1
    
    def isPrefix(self, searchWord, word):
        if len(searchWord) > len(word):
            return False
        for i,ch in enumerate(searchWord):
            chInWord = word[i]
            if ch != chInWord:
                return False
        return True