# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str) -> [int]:
        m = {}
        for i,ch in enumerate(S):
            m[ch] = i
        
        out = []
        startIdx = 0 # idx for start of partition
        endIdx = 0 # idx for end of partition
        for i,ch in enumerate(S):
            if m[ch] > endIdx:
                endIdx = m[ch]
            elif i >= endIdx:
                out.append(endIdx-startIdx+1)
                startIdx = i+1
                endIdx = i+1
        return out    