# https://leetcode.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chset = set()
        for i,ch in enumerate(s):
            if ch in chset:
                chset.remove(ch)
            else:
                chset.add(ch)
        
        if len(chset) <= 1:
            return True
        return False