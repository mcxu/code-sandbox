'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s)
        stack = []
        for i,ch in enumerate(sList):
            if ch == "(":
                stack.append((ch,i))
            elif ch == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((ch,i))
        
        # for each index in stack, set sList[index] to empty string
        for _,item in enumerate(stack):
            sList[item[1]] = ""
        
        return "".join(sList)