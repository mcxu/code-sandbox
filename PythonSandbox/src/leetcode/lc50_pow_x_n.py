# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x**1
        elif n == 0:
            return 1
        elif n < 0 or x <= 1:
            return x**n
        
        nhalf = int(n/2)
        result = self.myPow(x, nhalf)
        result *= result
        if int(n%2) > 0:
            result *= x
        return result