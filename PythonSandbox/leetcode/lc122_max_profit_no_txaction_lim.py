'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution:
    '''
    Let n = len(prices)
    Time complexity: O(n), iterate through all prices.
    Space complexity: 
    '''
    def maxProfit(self, prices):
        if not prices or len(prices)==1:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            currPrice = prices[i]
            prevPrice = prices[i-1]
            if currPrice > prevPrice:
                profit += (currPrice-prevPrice)
        #print("profit: ", profit)
        return profit
    
    def test1(self):
        prices = [7,1,5,3,6,4]
        # Correct Output: 7
        res = self.maxProfit(prices)
        print("test1 result: ", res)
        
    def test2(self):
        prices = [7,6,4,3,1]
        # Correct Output: 0
        res = self.maxProfit(prices)
        print("test2 result: ", res)