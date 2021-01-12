'''
https://leetcode.com/problems/container-with-most-water/
'''
class Solution:
    def maxArea(self, height: [int]) -> int:
        i = 0
        j = len(height)-1
        maxArea = 0
        while i < j:
            #print("i:{}, j:{}".format(i,j))
            minHeight = min(height[i], height[j])
            width = j-i
            area = minHeight*width
            maxArea = max(maxArea, area)
            
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
                
        return maxArea
        