""" https://leetcode.com/problems/coin-change/
Find minimum number of coins to make this change amount
"""
from typing import List

class Solution:
    """
    Dyanamic Programming
    Time complexity: O(amount * coins)
    Space complexity: O(amount)
    """
    def coinChange(self, coins: List[int], amount: int) -> int: 
        coins.sort()
        mncForAmt = [float('inf')] * (amount+1)
        mncForAmt[0] = 0

        for amt in range(amount+1):
            for denom in coins:
                if amt - denom >= 0:
                    mncForAmt[amt] = min(mncForAmt[amt], mncForAmt[amt-denom]+1)
                else:
                    break

        if mncForAmt[amount] == float('inf'):
            return -1

        return mncForAmt[amount]

    def test1(self):
        amount = 29
        coins = [1,5,10,12,25,50] 
        # expected: 3
        res = self.coinChange(coins, amount)
        print("res: ", res)

# s = Solution()
# s.test1()

#=======================================================================================

""" Recursive with memoization
Time complexity: O(len(coins)^amount)
Space complexity: O(amount)
    Recursive callstack: O(amount)
    memo: O(amount)
"""
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        numCoins = self.getMinCoins(coins, amount, memo)

        if numCoins == float('inf'):
            return -1
            
        return numCoins

    def getMinCoins(self, coins, amount, memo):
        if len(coins) == 0:
            return 0
        
        # if the amount is 0, then we need 0 coins
        if amount == 0: 
            return 0

        if amount in memo.keys():
            return memo[amount]

        # start at infinity because 0 coins is already the minimum, so start at the opposite end of that
        minNumCoinsForAmount = float('inf')
        for _,denom in enumerate(coins):
            if amount - denom >= 0:
                # min coins for the subproblem + 1 coin (the denom coin)
                minNumCoinsForDenom = self.getMinCoins(coins, amount-denom, memo) + 1 
                if minNumCoinsForDenom < minNumCoinsForAmount:
                    minNumCoinsForAmount = minNumCoinsForDenom
        
        memo[amount] = minNumCoinsForAmount
        return memo[amount]

    
    def test(self):
        cases = [
            # dict(coins=[1,2,5], amount=11, expected=3),
            #dict(coins=[2], amount=3, expected=-1),
            # dict(coins=[1,2,3], amount=4, expected=2),
            dict(coins=[1,5,10,12,25,50], amount=29, expected=3)
        ]

        for c in cases:
            res = self.coinChange(c["coins"], c["amount"])
            print("case: ", c)
            print("res: ", res)
            assert res == c["expected"]

sol = Solution2()
sol.test()
