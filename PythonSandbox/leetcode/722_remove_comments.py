# https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: [str]) -> [str]:
        refactored = []
        insideComment = False # used for comment block
        newline = None
        for _,line in enumerate(source):
            if insideComment==False:
                newline = []
            
            i=0
            while i<len(line):
                if line[i:i+2]=="/*" and insideComment==False:
                    insideComment=True
                    i+=1
                elif line[i:i+2]=="*/" and insideComment==True:
                    insideComment=False
                    i+=1
                elif line[i:i+2]=="//" and insideComment==False:
                    break
                elif newline!=None and insideComment==False:
                    newline.append(line[i])
                i += 1
            #print("newline after while: ", newline)
            if newline and insideComment==False:
                refactored.append("".join(newline))
        
        return refactored