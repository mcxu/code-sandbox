class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        
        # init array to store min number of ways for subproblems.
        mnc = [float("inf")] * (amount+1) # O(n) space
        mnc[0] = 0 # if n=0, then there are 0 number of coins needed.

        for i in range(len(mnc)): # O(n) time
            for j in range(len(coins)): # O(d) time
                d = coins[j]
                #print("i={} j={}, d={}".format(i,j,d))
                if i-d >= 0:
                    mnc[i] = min(mnc[i], mnc[i-d] + 1)
                    #print("mnc update:\n", mnc)
                else:
                    break
                    
        minWaysFinal = mnc[amount]
        if minWaysFinal == float("inf"):
            return -1
        return minWaysFinal