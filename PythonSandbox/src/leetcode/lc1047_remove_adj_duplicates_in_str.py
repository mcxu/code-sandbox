'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Input: "abbaca"
Output: "ca"
Explanation: bb is duplicate, delete bb, then aa is duplicate, delete aa. Left with ca.
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i+1 < len(S):
            #print("i={},    S: {}".format(i,S))
            if S[i] == S[i+1]:
                newS = S[:i] + S[i+2:]
                S = newS
                if i >= 1:
                    i -= 1
            else:
                i += 1
        #print("S final: ", S)
        return S
    
    def test1(self):
        #S = "abbaca"
        #S = "aabbccdd"
        S = "aabbbccd"
        res = self.removeDuplicates(S)
        print("test1 res: ", res)

s = Solution()
s.test1()