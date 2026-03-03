# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        pathSplit = path.split("/")
        # print("pathSplit: ", pathSplit)

        stack = []

        i = 0
        while i < len(pathSplit):
            currch = pathSplit[i]
            #print(f"i:{i} currch", currch)         
            if currch == "" or currch == ".":
                i += 1
                continue
            if currch == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(currch)
            i += 1

        canonicalPath = ""

        if not stack:
            return "/"
        
        while stack:
            canonicalPath = "/" + stack.pop() + canonicalPath

        return canonicalPath

