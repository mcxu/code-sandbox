'''
https://leetcode.com/problems/top-k-frequent-elements/
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for i,n in enumerate(nums):
            if n in freqMap.keys():
                freqMap[n] += 1
            else:
                freqMap[n] = 1
        
        # sort dictionary by value, return list of (key,value) tuples
        nToFreqTups = sorted(freqMap.items(), key=lambda item: item[1])
        topkElts = []
        for i in range(len(nToFreqTups)-1, len(nToFreqTups)-k-1, -1):
            topkElts.append(nToFreqTups[i][0])
        return topkElts