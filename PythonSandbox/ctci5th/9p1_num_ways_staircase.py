def numWays(n):
    if n==0:
        return 0
    
    dp = [0,1,2,3]
    if n<=3:
        return dp[n]

    for i in range(4, n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    return dp[n]

def test1():
    n = 20
    res = numWays(n)
    print("res: ", res)

test1()
