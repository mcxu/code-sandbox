'''
https://leetcode.com/problems/reverse-words-in-a-string/
Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words 
to a single space in the reversed string.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        sSplit = s.split(" ")
        
        outStr = ""
        for i in range(len(sSplit)-1, -1, -1):
            word = sSplit[i]
            if word:
                outStr += (word + " ")
        
        return outStr[:-1]
    
    def test1(self, alg):
        input1 = "the sky is blue"
        input2 = "  hello world!  "
        input3 = "a good   example"
        inputs = [input1, input2, input3]
        print("test1 results:")
        for inp in inputs:
            res = self.reverseWords(inp)
            print("input: {}\tres: {}".format(inp, res))

s = Solution()
alg = s.reverseWords
s.test1(alg)