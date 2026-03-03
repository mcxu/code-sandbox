'''
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for _,c in enumerate(s):
            if not stack:
                stack.append(c)
                continue
                
            if stack[-1]=="(" and c==")":
                stack.pop()
            elif stack[-1]=="{" and c=="}":
                stack.pop()
            elif stack[-1]=="[" and c=="]":
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0