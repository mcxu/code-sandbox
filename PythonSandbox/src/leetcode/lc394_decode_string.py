'''
https://leetcode.com/problems/decode-string/
'''
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        
        stack = [s[0]]
        dcStr = ""
        i = 1
        while i < len(s):
            ch = s[i]
            stack.append(ch)
            
            if stack[-1] == "]":
                stack.pop() # pop off closing bracket
                backtrackedStr, stack = self.goToOpenBracket(stack)
                
                k = ""
                if stack:
                    stack.pop() # pop off opening bracket
                    while stack and stack[-1].isnumeric():
                        k = stack.pop() + k # pop off k
                    k = int(k)
                else:
                    k = 1
                    
                #print("stack B: ", stack)
                decodedSection = k * backtrackedStr[::-1]
                #print("dcStr B: ", dcStr)
                for ch in decodedSection:
                    stack.append(ch)
                #print("stack after adding back: ", stack)
            
            i += 1 
                
        return "".join(stack)
            
    def goToOpenBracket(self, stack):
        string = ""
        while stack and stack[-1] != "[":
            string += stack.pop()
        return string, stack