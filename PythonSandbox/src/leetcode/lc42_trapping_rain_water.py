'''
https://leetcode.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: [int]) -> int:
        rain = [0] * len(height)
        if not height:
            return sum(rain)
        
        maxHeight = max(height)
        mhInd = height.index(maxHeight)
        #print("mhInd: ", mhInd)
        
        # from left
        maxSoFar = 0
        for i,h in enumerate(height[:mhInd]):
            if h > maxSoFar:
                maxSoFar = h
            elif h < maxSoFar:
                rain[i] = maxSoFar-h
        #print("rain: ",  rain)
        
        # from right
        maxSoFar = 0
        for i in range(len(height)-1, mhInd-1, -1):
            h = height[i]
            if h > maxSoFar:
                maxSoFar = h
            elif h < maxSoFar:
                rain[i] = maxSoFar-h
        #print("rain final: ", rain)
        
        return sum(rain)
    
    def test1(self):
        input = [0,1,0,2,1,0,1,3,2,1,2,1]
        #outputExpected = 6
        res = self.trap(input)
        print("res: ", res)

s = Solution()
s.test1()