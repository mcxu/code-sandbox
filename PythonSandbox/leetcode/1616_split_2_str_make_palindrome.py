# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        arev = a[::-1]
        brev = b[::-1]
        
        if len(a)==1 or len(b)==1:
            return True
        
        i = 0
        while i < len(a):
            ach = a[i]
            brevch = brev[i]
            if ach != brevch:
                break
            i += 1
        # print("match")
        # print("apref: ", a[:i])
        # print("brefpref: ", brev[:i])
        if i >= 1:
            return True
        
        i = 0
        while i < len(b):
            bch = b[i]
            arevch = arev[i]
            if bch != arevch:
                break
            i += 1
        # print("match")
        # print("bpref: ", b[:i])
        # print("arevpref: ", arev[:i])
        if i >= 1:
            return True
        
        return False