# https://leetcode.com/problems/knight-probability-in-chessboard/

# brute force: TLE
class Solution:
    
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        d = 0
        probs = {}
        self.moveKnight(N,K,r,c,visited, d, probs)
        #print("probs: ")
        
        totprob = 1
        for depth in probs.keys():
            numerator = probs[depth][0]
            denom = probs[depth][1]
            totprob *= (numerator/denom)
        
        return totprob
    
    def moveKnight(self, N, K, r, c, visited, d, probs):
        #print("r:{}, c:{}".format(r,c))
        if r<0 or r>N-1 or c<0 or c>N-1:
            return 
        if K <= 0:
            return
        if visited[r][c]==d: # prevent cycles
            return 
        
        visited[r][c]==d
        
        n = 0 # numerator
        # up,right
        if r-2>=0 and c+1<=N-1: 
            n += 1
        # up,left
        if r-2>=0 and c-1>=0: 
            n += 1
        # right,up
        if c+2<=N-1 and r-1>=0:
            n += 1
        # left,up
        if c-2>=0 and r-1>=0:
            n += 1
        # left,down
        if c-2>=0 and r+1<=N-1:
            n += 1
        # down,left
        if r+2<=N-1 and c-1>=0:
            n += 1
        # down,right
        if r+2<=N-1 and c+1<=N-1:
            n += 1
        # right,down
        if c+2<=N-1 and r+1<=N-1:
            n += 1
            
        if d in probs:
            currprob = probs[d]
            currnum = currprob[0]
            currdenom = currprob[1]
            probs[d] = [currnum+n, currdenom+8]
        else:
            probs[d] = [n, 8]
        
        self.moveKnight(N,K-1,r-2,c+1,visited,d+1,probs)
        self.moveKnight(N,K-1,r-2,c-1,visited,d+1,probs)
        self.moveKnight(N,K-1,r-1,c+2,visited,d+1,probs)
        self.moveKnight(N,K-1,r-1,c-2,visited,d+1,probs)
        self.moveKnight(N,K-1,r+1,c-2,visited,d+1,probs)
        self.moveKnight(N,K-1,r+2,c-1,visited,d+1,probs)
        self.moveKnight(N,K-1,r+2,c+1,visited,d+1,probs)
        self.moveKnight(N,K-1,r+1,c+2,visited,d+1,probs)