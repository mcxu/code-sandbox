# Iterative DP solution
class Solution_Iterative:
    def minDays(self, n: int) -> int:
        auxInit = [0,1,2,2]
        if n <= 3:
            return auxInit[n]
        
        aux = [0 for _ in range(n+1)]
        for i,c in enumerate(auxInit):
            aux[i]=c
        
        for c in range(4, n+1):
            # mdUpToDay = 1+aux[c-1] # min days up to current day
            # if c%6==0:
            #     mdUpToDay = 1+min(aux[c-1], aux[c-int(c/2)], aux[c-2*int(c/3)])
            # elif c%3==0:
            #     mdUpToDay = 1+min(aux[c-1], aux[c-2*int(c/3)])
            # elif c%2==0:
            #     mdUpToDay = 1+min(aux[c-1], aux[c-int(c/2)])
            aux[c] = 1 + min(c%2+aux[int(c/2)], c%3+aux[int(c/3)])
        return aux[n]

# Recursive solution
class Solution_Recursive:
    def minDays(self, n: int) -> int:
        memo = {}
        md = self.helper(n, memo)
        return md
    
    def helper(self, c, memo):
        if c == 0:
            return 0
        if c == 1:
            return 1
        if c == 2:
            return 2
        if c == 3:
            return 2

        if c in memo.keys():
            #print("memo key: {}, val: {}".format(c, memo[c]))
            return memo[c]

        if c % 6 == 0:
            memo[c] = 1+min(self.helper(c-1, memo), self.helper(c-int(c/2), memo), self.helper(c-2*int(c/3), memo))
        elif c % 3 == 0:
            memo[c] = 1+min(self.helper(c-1, memo), self.helper(c-2*int(c/3), memo))
        elif c % 2 == 0:
            memo[c] = 1+min(self.helper(c-1, memo), self.helper(c-int(c/2), memo))
        else:
            memo[c] = 1+self.helper(c-1, memo)
            
        return memo[c]
    
# def test1(self):
#     #n = 820592
#     #n = 1000
#     #n = 3681069
#     n = 9209408
#     res = self.minDays(n)
#     print("res: ", res)

# s = Solution()
# s.test1()