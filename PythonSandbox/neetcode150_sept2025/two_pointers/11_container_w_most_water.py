from typing import List

class ContainerWithMostWater:
    """
    Time complexity: O(n) because i < j constraint so height array is iterated once at most.
    Space complexity: O(1) because the variables used only save single values.
    """
    def maxArea(self, height: List[int]) -> int:
        maxAreaSoFar = 0

        i = 0
        j = len(height)-1
        while i < j:
            iHeight = height[i]
            jHeight = height[j]

            area = 0
            if iHeight >= jHeight:
                area = jHeight * (j - i)
                j -= 1
            else:
                area = iHeight * (j - i)
                i += 1

            maxAreaSoFar = max(maxAreaSoFar, area)
        
        return maxAreaSoFar
