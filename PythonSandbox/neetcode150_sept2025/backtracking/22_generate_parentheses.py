class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        validPerms = []
        allPerms = set()
        symbols = ["(",")"] * n
        self.permute(symbols, allPerms, validPerms)
        return ["".join(e) for e in validPerms]

    def permute(self, symbols, allPerms, validPerms):
        symbolsTup = tuple(symbols)
        if symbolsTup in allPerms:
            return
        
        allPerms.add(symbolsTup)
        print("allPerms: ", allPerms)

        if self.isValid(symbolsTup):
            validPerms.append(symbolsTup)
        
        for i in range(len(symbols)-1):
            symbols[i], symbols[i+1] = symbols[i+1], symbols[i]
            self.permute(symbols, allPerms, validPerms)
            symbols[i], symbols[i+1] = symbols[i+1], symbols[i]
        return
        
    def isValid(self, symbols):
        stack = []
        for i in range(len(symbols)):
            s = symbols[i]
            if stack and stack[-1] == "(" and s == ")":
                stack.pop()
            else:
                stack.append(s)
        return not stack

    def test1(self):
         n = 3
         result = self.generateParenthesis(n)
         print("result: ", result)

if __name__ == "__main__":
    s = Solution()
    s.test1()