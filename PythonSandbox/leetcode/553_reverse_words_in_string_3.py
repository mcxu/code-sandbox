'''
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string, you need to reverse the order of characters in each word within 
a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be 
any extra space in the string.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        sSplit = s.split(" ")
        outStr = ""
        for word in sSplit:
            if word:
                outStr += (self.revString(word) + " ")
        return outStr[:-1]
    
    def revString(self, s):
        sRev = ""
        for i in range(len(s)-1, -1, -1):
            sRev += s[i]
        return sRev

    def test1(self, alg):
        input = "Let's take LeetCode contest"
        res = alg(input)
        print("test1 res: ", res)

s = Solution()
alg = s.reverseWords
s.test1(alg)