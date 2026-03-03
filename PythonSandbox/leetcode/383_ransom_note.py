'''
383. Ransom Note (https://leetcode.com/problems/ransom-note/)

Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false. Each letter in the magazine string can only be used once in your ransom note.
You may assume that both strings contain only lowercase letters.

Sample input:
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap = {} # char:freq
        for i in range(len(magazine)):
            char = magazine[i]
            if char in charMap.keys():
                charMap[char] += 1
            else:
                charMap[char] = 1
        
        # evaluate ransomNote
        for i in range(len(ransomNote)):
            ranChar = ransomNote[i]
            if ranChar in charMap.keys():
                charMap[ranChar] -= 1
                if charMap[ranChar] < 0:
                    return False
            else:
                return False
        return True