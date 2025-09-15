# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

import heapq

class Solution:
    def shortestSubarray(self, A: [int], K: int) -> int:
        heap = [(0,-1)] # (runSum, index)
        runSum = 0 # running sum
        shortest = float('inf')
        for i in range(len(A)):
            n = A[i]
            runSum += n
            #print("---i:{}, n: {}, runSum: {}".format(i, n ,runSum))
            #print("heap: ", heap)
            while heap and runSum-heap[0][0] >= K:
                #print("runSum >= K")
                mostRecentIdx = heapq.heappop(heap)[1]
                #print("mostRecentIdx: ", mostRecentIdx)
                shortest = min(shortest, i-mostRecentIdx)
                #print("runSum: {}, shortest: {}".format(runSum, shortest))
            
            heapq.heappush(heap, (runSum, i))
            #print("heap end of for: ", heap)
            
        if shortest == float('inf'):
            return -1
        
        return shortest