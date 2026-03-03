'''
https://leetcode.com/problems/palindrome-removal/
'''
class Solution:
    def minimumMoves(self, arr: [int]) -> int:
        dp  = [[float('inf') for _ in range(len(arr))] for _ in range(len(arr))]
        
        for i in range(len(arr)-1, -1, -1):
            for j in range(i, len(arr)):
                #print("--- i:{}, j:{}".format(i,j))
                #print("arr[i]={}, arr[j]={}".format(arr[i],arr[j]))
                if i==j:
                    dp[i][j]=1
                elif i+1==j:
                    if arr[i]==arr[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 2
                else:
                    # case: [1,2,3,1] where i=0,j=3
                    if arr[i] == arr[j]:
                        dp[i][j] = dp[i+1][j-1] # if arr[i]==arr[j], the current numbers don't matter, so just use result from inner subproblem.
                    else:
                        dp[i][j] = dp[i+1][j-1]+2
                    
                    # case: [3,1,2,1] where i=0,j=3. remove 3(1mv), then 1,2,1(1mv) 
                    dp[i][j] = min(dp[i][j], 1+dp[i+1][j])
                    
                    # case: [1,2,1,3] where i=0,j=3, remove 1,2,1(1mv), then 3(1mv)
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
                    
                    # case: [1,2,1,3,4,3], i=0,j=5. remove 1,2,1(1mv), then 3,4,3(1mv)
                    # case: [1,2,1,5,3,4,3],i=0,j=5. remove 1,2,1(1mv), then 5(1mv), then 3,4,3(1mv)
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])

        return dp[0][-1]
    
    def test1(self, alg):
        #arr = [1,2] # expected: 2
        #arr = [1,3,4,1,5] # expected: 3
        arr = [16,13,13,10,12] # expected: 4
        #arr = [1,2,3,1]
        #arr = [1,1,1]
        res = alg(arr)
        print("res: ", res)

    def test2(self, alg):
        # without the for loop from i:k, k+1:j, this case fails.
        arr = [1,4,1,1,2,3,2,1] # expected: 2


s = Solution()
alg = s.minimumMoves
s.test1(alg)