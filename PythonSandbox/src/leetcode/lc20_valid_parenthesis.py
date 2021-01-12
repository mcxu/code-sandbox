'''
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i,ch in enumerate(s):   
            if stack:
                if stack[-1] == "(" and ch == ")":
                    stack.pop()
                elif stack[-1] == "{" and ch == "}":
                    stack.pop()
                elif stack[-1] == "[" and ch == "]":
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
                
        if stack:
            return False
        return True