'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
'''

class Solution:
    def reverse(self, x: int) -> int:
        xStr = str(x)
        neg = False
        if x < 0:
            xStr = xStr[1:]
            neg = True
        
        #reverse xStr
        revStr = ""
        xLen = len(xStr)
        for i in range(xLen): 
            revStr += xStr[xLen-1-i]
        revInt = int(revStr)
        
        # must check for max int limit
        if revInt > ((2**31) - 1):
            return 0
        if neg:
            revInt *= -1
        
        return revInt
        
    def test1(self, alg):
        #x = 123
        x = -123
        #x = 120
        #x = 1534236469 # lc says the answer should be 0, is this a bug?
        revx = self.reverse(x)
        print("test1 revx: ", revx)

sol = Solution()
sol.test1(sol.reverse)

        
