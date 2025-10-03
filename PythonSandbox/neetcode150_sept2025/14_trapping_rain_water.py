from typing import List

class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        highestIdx = height.index(max(height))
        trappedFromLeft = self.getWater(height, 0, highestIdx+1)
        trappedFromRight = self.getWater(height, len(height)-1, highestIdx-1)
        return trappedFromLeft + trappedFromRight
    
    def getWater(self, height: List[int], startIdx, endIdx) -> int:
        trapped = 0
        highestSoFar = 0
        direction = 1 if startIdx <= endIdx else -1
        for i in range(startIdx, endIdx, direction):
            barHeight = height[i]
            diff = highestSoFar - barHeight
            if diff > 0:
                trapped += diff
            highestSoFar = max(highestSoFar, barHeight)
        return trapped