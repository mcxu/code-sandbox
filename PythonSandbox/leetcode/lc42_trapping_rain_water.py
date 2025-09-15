'''
https://leetcode.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: [int]) -> int:
        totalWater = 0

        maxHeightIdx = height.index(max(height))

        # moving from 0 to max height idx
        highestBarSoFar = 0
        for i in range(0, maxHeightIdx):
            barHeight = height[i]

            if barHeight > highestBarSoFar:
                highestBarSoFar = barHeight
            else:
                totalWater += (highestBarSoFar - height[i])
        
        # moving from right to max height idx
        highestBarSoFar = 0
        for i in range(len(height)-1, maxHeightIdx, -1):
            barHeight = height[i]

            if barHeight > highestBarSoFar:
                highestBarSoFar = barHeight
            else:
                totalWater += (highestBarSoFar - height[i])
        
        return totalWater
    
    def test1(self):
        input = [0,1,0,2,1,0,1,3,2,1,2,1]
        #outputExpected = 6
        res = self.trap(input)
        print("res: ", res)

s = Solution()
s.test1()