'''
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
'''

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        hcuts = sorted(horizontalCuts)
        vcuts = sorted(verticalCuts)

        if hcuts[-1] < h:
            hcuts.append(h)
        if vcuts[-1] < w:
            vcuts.append(w)
            
        hIntMax = 0
        for i in range(len(hcuts)):
            interval = hcuts[i]
            if i > 0:
                interval -= hcuts[i-1]
            if interval > hIntMax:
                hIntMax = interval
        
        vIntMax = 0
        for j in range(len(vcuts)):
            interval = vcuts[j]
            if j > 0:
                interval -= vcuts[j-1]
            if interval > vIntMax:
                vIntMax = interval
        
        return (hIntMax * vIntMax)%(10**9 + 7)