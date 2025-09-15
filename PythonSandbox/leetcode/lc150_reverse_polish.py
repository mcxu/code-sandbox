'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ["+", "-", "*", "/"]
        stack = []
        for i,t in enumerate(tokens):
            if t in symbols:
                n2 = stack.pop()
                n1 = stack.pop()
                #print("n1: {}, n2: {}".format(n1,n2))
                if t == "+":
                    res = n1+n2
                    stack.append(res)
                elif t == "-":
                    res = n1-n2
                    stack.append(res)
                elif t == "*":
                    res = n1*n2
                    stack.append(res)
                elif t == "/":
                    res = int(n1/n2)
                    stack.append(res)
            else:
                stack.append(int(t))
        
        return stack[0]