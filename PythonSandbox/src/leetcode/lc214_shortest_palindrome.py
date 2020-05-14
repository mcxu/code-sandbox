'''
Given a string s, you are allowed to convert it to a palindrome by adding characters 
in front of it. Find and return the shortest palindrome you can find by performing 
this transformation.

Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: "abcd"
Output: "dcbabcd"
'''

class Solution:
    # brute force solution: time limit exceeded
    def shortestPalindrome(self, s: str) -> str:
        # find ending index of longest palindrome that already exists in s
        i = len(s)-1
        j = 0 # pal End ind
        while i > 0:
            if self.isPal(s, 0, i):
                j = i
                break
            i -= 1

        snew = s[j+1:][::-1] + s
        return snew

    def isPal(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def test1(self):
        #input = "aacecaaa"
        input = "abcd"
        res = self.shortestPalindrome(input)
        print("test1 res: ", res)
    
    def test2(self):
        #input = "abbacd" # Expected dcabbacd
        #input = "abcbabcab" # Expected bacbabcbabcab
        #input = "aaaaa"
        input = "asdffdsarrqt"
        res = self.shortestPalindrome(input)
        print("test2 res: ", res)

s = Solution()
#s.test1()
s.test2()