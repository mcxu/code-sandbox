class Solution:
    def getDescentPeriods(self, prices: [int]) -> int: 
        periods = [1] * len(prices)

        for i in range(1, len(prices)):
            prevPrice = prices[i-1]
            currPrice = prices[i]

            if currPrice == prevPrice-1:
                periods[i] = periods[i-1]+1
        
        return periods