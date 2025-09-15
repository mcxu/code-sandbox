# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        slist = list(s.strip())
        
        #remove empty str
        i = 0
        while i < len(slist):
            if slist[i]=='' or slist[i]==' ':
                slist.pop(i)
                i -= 1
            i += 1
        
        # merge multi-digit numbers
        i = 0
        while i < len(slist)-1:
            curr = slist[i]
            nxt = slist[i+1]
            if curr.isnumeric() and nxt.isnumeric():
                slist[i] = curr+nxt
                slist.pop(i+1)
                i -= 1
            i += 1
            
        multDiv = set(['*', '/'])
        addSub = set(['+', '-'])
        i = 0
        while i < len(slist):
            curr = slist[i]
            if curr in multDiv:
                left = slist[i-1]
                right = slist[i+1]
                res = 0
                if curr == "*":
                    res = int(left)*int(right)
                elif curr == "/":
                    res = int(int(left)/int(right))   
                slist[i-1]=res
                slist.pop(i);slist.pop(i)
                i -= 1
            i += 1
        
        i = 0
        while i < len(slist):
            curr = slist[i]
            if curr in addSub:
                left = slist[i-1]
                right = slist[i+1]
                res = 0
                if curr == "+":
                    res = int(left)+int(right)
                elif curr == "-":
                    res = int(left)-int(right)   
                slist[i-1]=res
                slist.pop(i);slist.pop(i)
                i -= 1
            i += 1    
        
        return int(slist[0])