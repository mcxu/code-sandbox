# https://leetcode.com/problems/powx-n/

class Solution:
    # using exponentiation
    # Time complexity: O(log n) bc while loop is using nn <= 0 as stopping criteria and nn is being //2
    # Space complexity: O(1) bc we are storing just nn and result, 2 variables.
    def myPow(self, x: float, n: int) -> float:
        result = 1
        nn = abs(n)

        while nn > 0:
            if nn % 2 == 1:
                result = result * x
                nn = nn - 1
            else:
                x = x * x
                nn = nn // 2
        
        if n < 0:
            return 1/result

        return result
