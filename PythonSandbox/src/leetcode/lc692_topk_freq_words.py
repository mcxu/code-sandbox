'''
https://leetcode.com/problems/top-k-frequent-words/
'''

import heapq

class Solution:
    '''
    time: O(n + k*logn)
    space: O(n)
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = {} # O(n) space
        for w in words: # O(n) time
            if w in m.keys():
                m[w] += 1
            else:
                m[w] = 1
        
        #print("items: ", m.items())
        tups = [(-freq, word) for (word, freq) in m.items()] # O(n) space
        #print("tups: ", tups)
        
        heapq.heapify(tups) # O(n) time
        #print("tups after heapify: ", tups)
        
        topk = []
        for i in range(k): # O(k*logn) time
            tup = heapq.heappop(tups)
            topk.append(tup[1])
        return topk