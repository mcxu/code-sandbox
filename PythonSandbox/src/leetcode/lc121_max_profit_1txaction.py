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
        if not prices or len(prices) == 1:
            return 0
        
        minBuyInd = 0
        maxSellInd = 1
        profitSoFar = 0
        for i in range(1, len(prices)):
            #print("i={}".format(i))
            
            sellPrice = prices[i]
            if sellPrice > prices[maxSellInd]:
                maxSellInd = i
                #print("maxSellInd now: ", maxSellInd)
            
            buyPrice = prices[i-1]
            if buyPrice < prices[minBuyInd]:
                minBuyInd = i-1
                #print("minBuyInd now: ", minBuyInd)
                
            if minBuyInd >= maxSellInd:
                #print("mbi and msi crossed")
                maxSellInd = i

            profitSoFar = max(profitSoFar, prices[maxSellInd]-prices[minBuyInd])
        
        return profitSoFar
    
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
