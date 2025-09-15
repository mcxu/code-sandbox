'''
https://leetcode.com/problems/container-with-most-water/
'''
class Solution:
    def maxArea(self, height: [int]) -> int:
        i = 0
        j = len(height)-1

        maxWater = 0

        while i < j:
            leftHeight = height[i]
            rightHeight = height[j]

            minHeight = min(leftHeight, rightHeight)
            maxWater = max(maxWater, (j-i) * minHeight)
            
            if leftHeight < rightHeight:
                i += 1
            else:
                j -= 1
        
        return maxWater

    def test(self):
        cases = [
            { "height": [1,8,6,2,5,4,8,3,7], "ans": 49 },
            { "height": [1,1], "ans": 1 }
        ]

        for case in cases:
            res = self.maxArea(case["height"])
            print("res: ", res)
            assert res == case["ans"]
    

sol = Solution()
sol.test()
