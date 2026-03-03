class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            countEven = self.expand(s, i, i+1)
            countOdd = self.expand(s, i, i)
            count += countEven + countOdd
        
        return count

    def expand(self, s, i, j):
        count = 0
        while i>=0 and j<=len(s)-1 and s[i]==s[j]:
            count += 1
            i -= 1
            j += 1
        return count
