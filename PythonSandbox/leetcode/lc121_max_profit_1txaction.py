'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    '''
    Let n = len(prices)
    Time complexity: O(n), for loop iterates through all prices.
    Space complexity: O(1), profitsSoFar only stores most recent max profit.
        minBuyInd and maxSellInd only stores, the index of min price and max price
        up to the current iterated price.
    '''
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices or len(prices)==1:
            return 0
        
        buyIdx = 0 # minimize value at this index
        sellIdx = 1 # maximize value at this index
        maxProfitSoFar = 0
        for i in range(1, len(prices)):
            currPrice = prices[i]

            if currPrice < prices[buyIdx]:
                buyIdx = i
            
            if currPrice > prices[sellIdx]:
                sellIdx = i

            if buyIdx >= sellIdx:
                print(f"buyIdx caught up to sellIdx: buyIdx: {buyIdx}, sellIdx: {sellIdx}, currIdx: {i}")
                sellIdx = i

            profitSoFar = prices[sellIdx] - prices[buyIdx]
            maxProfitSoFar = max(maxProfitSoFar, profitSoFar)
        
        return maxProfitSoFar
    
    def test1(self):
        prices = [7,1,5,3,6,4]
        # Correct Output: 5
        res = self.maxProfit(prices)
        print("test1 result: ", res)
        
    def test2(self):
        prices = [7,6,4,3,1]
        # Correct Output: 0
        res = self.maxProfit(prices)
        print("test2 result: ", res)

s = Solution()
s.test1()
#s.test2()
