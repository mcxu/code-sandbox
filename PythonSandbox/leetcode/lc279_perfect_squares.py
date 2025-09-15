# https://leetcode.com/problems/perfect-squares/

import math

class Solution:
    def numSquares(self, n: int) -> int:
        sqNums = [x**2 for x in range(int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for j in range(len(sqNums)):
                sqn = sqNums[j]
                #print("i: {}, j: {}, sqn: {}".format(i, j, sqn))
                if i-sqn >= 0:
                    dp[i] = min(dp[i], dp[i-sqn]+1)
                else:
                    break
        return dp[-1]