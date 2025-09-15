# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        sList = list("()"*n)
        #print("sList: ", sList)
        allPerms = set()
        wellFormedPerms = []
        self.permute(sList, allPerms, wellFormedPerms)
        return wellFormedPerms
        
    def permute(self, sList, allPerms, wellFormedPerms):
        s = "".join(sList)
        if s in allPerms:
            return
        else:
            allPerms.add(s)
        
            #check if sList is wellFormed
            if self.isWellFormed(s):
                wellFormedPerms.append(s)
        
        for i in range(len(sList)-1):
            sList[i],sList[i+1] = sList[i+1],sList[i]
            self.permute(sList, allPerms, wellFormedPerms)
            sList[i],sList[i+1] = sList[i+1],sList[i]
    
    def isWellFormed(self, sTup):
        stack = []
        for i,p in enumerate(sTup):
            if stack:
                if stack[-1]=="(" and p==")":
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        if stack:
            return False
        return True