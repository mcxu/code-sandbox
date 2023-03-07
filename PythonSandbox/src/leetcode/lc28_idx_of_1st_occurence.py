class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i,c in enumerate(haystack):
            if c == needle[0]:
                checkResult = self.check(haystack, needle, i)
                if checkResult == True:
                    return i
        return -1

    def check(self, haystack, needle, i):
        j = 0
        while i<len(haystack) and j<len(needle) and haystack[i] == needle[j]:
            i += 1
            j += 1
        if j >= len(needle) and haystack[i-1] == needle[j-1]:
            return True

        return False
        