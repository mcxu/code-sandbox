"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
"""

from typing import List

class Solution2:
    """ This solution passes.
    Let n ~ len(prices), k = total num of transactions allowed
    Time complexity: O(n*k)
    Space complexity: O(n*k)
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profits = [[0 for _ in range(n)] for _ in range(k+1)]

        for t in range(1, k+1):
            maxSoFarFortTxns = -float('inf')
            for d in range(1, n):
                maxSoFarFortTxns = max(maxSoFarFortTxns, profits[t-1][d-1] - prices[d-1])
                notTransact = profits[t][d-1]
                transact = prices[d] + maxSoFarFortTxns
                profits[t][d] = max(notTransact, transact)
        
        return profits[k][n-1]
    
class Solution:
    """ Warning: This solution causes TLE
    Let n ~ len(prices), k = total num of transactions allowed
    Time complexity: O(n^2 * k)
    Space complexity: O(n * k), due to the profits auxiliary matrix
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profits = [[0 for _ in range(n)] for _ in range(k+1)]

        for t in range(1, k+1): # iterate row
            for d in range(1, n): # iterate column
                
                # if not transact, then max profit is same as previous day's profit
                notTransact = profits[t][d-1] 

                # if transact, then max profit is the days price + max(list of profits up to day d)
                transact = prices[d] + max([profits[t-1][x] - prices[x] for x in range(d)])

                # take the max of profit from not transacting vs transacting
                profits[t][d] = max(notTransact, transact)
        
        return profits[k][n-1]