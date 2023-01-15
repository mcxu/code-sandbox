# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        chset = set()
        for _,ch in enumerate(s):
            if ch in chset:
                chset.remove(ch)
            else:
                chset.add(ch)
        
        if len(chset) <= k:
            return True
        return False