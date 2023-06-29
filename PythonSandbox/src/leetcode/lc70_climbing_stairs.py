""" count down with memo
Time complexity: O(n), n = number of stairs
Space complexity: O(n)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helper(n, memo):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            if n in memo.keys():
                return memo[n]
            
            take1 = helper(n-1, memo)
            take2 = helper(n-2, memo)
            memo[n] = take1+take2
            return memo[n]
        
        memo = {}
        return helper(n, memo)
    
    def test(self):
        pass

# count up with memo
class Solution2:
    def climbStairs(self, n: int) -> int:
        memo = {}
        numWays = self.helper(0, n, memo)
        return numWays
    
    def helper(self, i, n, memo):
        if i > n:
            return 0
        
        if i == n:
            return 1
        
        if i in memo:
            return memo[i]

        take1Step = self.helper(i+1, n, memo)
        take2Steps = self.helper(i+2, n, memo)
        memo[i] = take1Step + take2Steps
        return memo[i]

""" Dynamic programming
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution3:
    def climbStairs(self, n: int) -> int:
        numSteps = [1, 1]

        if n <= len(numSteps)-1:
            return numSteps[n]

        i = 2
        while i <= n:
            tempSecond = numSteps[-1]
            numSteps[-1] = numSteps[-2] + numSteps[-1]
            numSteps[-2] = tempSecond
            i += 1

        return numSteps[-1]
