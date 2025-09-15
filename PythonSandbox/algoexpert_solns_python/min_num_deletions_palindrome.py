"""
Minimum number of deletions to turn a string into a palindrome.
https://www.techiedelight.com/find-minimum-number-deletions-convert-string-into-palindrome/
"""

class Solution:
    def minNumOfDeletions(self, s):
        lo = 0
        hi = len(s)-1
        # numDeletions = self.remove(s, lo, hi)
        memo = {}
        numDeletions = self.removeWithMemo(s, lo, hi, memo)
        return numDeletions

    def remove(self, s, lo, hi):
        if not (0 <= lo <= len(s)-1) or not (0 <= hi <= len(s)-1):
            return 0
        
        if lo >= hi:
            return 0
        
        if s[lo] == s[hi]:
            removeBoth = self.remove(s, lo+1, hi-1)
            return removeBoth

        removeLower = self.remove(s, lo+1, hi)
        removeUpper = self.remove(s, lo, hi-1)
        return 1 + min(removeLower, removeUpper)

    def removeWithMemo(self, s, lo, hi, memo):
        if not (0 <= lo <= len(s)-1) or not (0 <= hi <= len(s)-1):
            return 0
        
        if lo >= hi:
            return 0
        
        if (lo,hi) in memo.keys():
            return memo[(lo,hi)]

        if s[lo] == s[hi]:
            removeBoth = self.removeWithMemo(s, lo+1, hi-1, memo)
            return removeBoth

        removeLower = self.removeWithMemo(s, lo+1, hi, memo)
        removeUpper = self.removeWithMemo(s, lo, hi-1, memo)
        memo[(lo,hi)] =  1 + min(removeLower, removeUpper)
        return memo[(lo,hi)]


    def test(self):
        s = "ACBCDBAA" # expected: 3
        #s = "aaaacba" # expected 2
        result = self.minNumOfDeletions(s)
        print("result: ", result)

s = Solution()
s.test()
