from typing import List

class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 1000000000
        lowestIdx = 0
        highestPrice = 0
        highestIdx = 0
        maxProfitSoFar = 0

        for i,price in enumerate(prices):
            if price < lowestPrice:
                lowestPrice = price
                lowestIdx = i

            if price > highestPrice:
                highestPrice = price
                highestIdx = i

            if lowestIdx >= highestIdx:
                highestIdx = lowestIdx
                highestPrice = prices[highestIdx]

            maxProfitSoFar = max(maxProfitSoFar, highestPrice - lowestPrice)
        
        return maxProfitSoFar
