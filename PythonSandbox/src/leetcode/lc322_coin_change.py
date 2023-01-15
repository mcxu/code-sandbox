# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        coins.sort()
        
        # keep track of min number of coins up to an amount, which is the index of this array
        mncUpToAmt = [float('inf')] * (amount+1)
        mncUpToAmt[0] = 0
        
        for i in range(1, amount+1):
            for _,denom in enumerate(coins):
                if i-denom >= 0:
                    mncUpToAmt[i] = min(mncUpToAmt[i], mncUpToAmt[i-denom]+1)
                    #print("mncUpToAmt: ", mncUpToAmt)
                else:
                    break
                    
        if mncUpToAmt[amount] == float('inf'): return -1
        return mncUpToAmt[amount]
    

    # version of algorithm to keep track of coins
    # http://www.cs.uni.edu/~fienup/cs270s04/lectures/lec6_1-29-04_coin_change_web.htm
    def coinChangeGetCoins(self, coins, amount):
        coins.sort()

        # min num of coins for an amount (index)
        mncUpToAmt = [float('inf')] * (amount+1)
        mncUpToAmt[0] = 0
        
        # keep track of which coins is needed
        coinArr = [0] * (amount+1)

        for i in range(1, amount+1):
            print("--- i: ", i)
            possibleSolnsFori = []
            denomForMncFori = float('inf')
            for j in range(len(coins)):
                denom = coins[j]
                if i-denom>=0:
                    possibleSolnsFori.append(mncUpToAmt[i-denom])
                    print("possibleSolnsFori: ", possibleSolnsFori)
                    print(" denom: ", denom)
                    if mncUpToAmt[i-denom] < denomForMncFori and denom > 1:
                        denomForMncFori = denom
                        print("denomForMncFori: ", denomForMncFori)
            
            if possibleSolnsFori:
                mncUpToAmt[i] = min(possibleSolnsFori)+1
                coinArr[i] = denomForMncFori

        print("mncUpToAmt: ", mncUpToAmt)
        print("coinArr:    ", coinArr)

        if mncUpToAmt[amount]==float('inf'): return [-1, -1]
        soln = [mncUpToAmt[amount], -1]
        return soln

    def test1(self):
        amount = 29
        coins = [1,5,10,12,25,50]
        res = self.coinChangeGetCoins(coins, amount)
        print("res: ", res)

s = Solution()
s.test1()