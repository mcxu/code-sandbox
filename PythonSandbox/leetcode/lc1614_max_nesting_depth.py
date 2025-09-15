# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        slist = list(s)
        slist = self.filter(slist)
        stack = []
        d = 0
        for i,ch in enumerate(slist):
            if stack and stack[-1]=="(":
                if ch == ")":
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
            
            d = max(d, len(stack))
            
        return d
        
        
    def filter(self, slist):
        arr = []
        for i in range(len(slist)):
            if slist[i]=="(" or slist[i]==")":
                arr.append(slist[i])
        return arr