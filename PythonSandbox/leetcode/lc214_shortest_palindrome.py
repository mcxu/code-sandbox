'''
https://leetcode.com/problems/shortest-palindrome/
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        srev = s[::-1]
        for i in range(len(s)):
            if srev[i:] == s[:len(s)-i]:
                return srev[:i] + s
        return ""

    def test1(self):
        #input = "aacecaaa"
        input = "abcd"
        res = self.shortestPalindrome(input)
        print("test1 res: ", res)
    
    def test2(self):
        #input = "abbacd" # Expected dcabbacd
        #input = "abcbabcab" # Expected bacbabcbabcab
        #input = "aaaaa"
        #input = "asdffdsarrqt"
        res = self.shortestPalindrome(input)
        print("test2 res: ", res)

s = Solution()
#s.test1()
s.test2()