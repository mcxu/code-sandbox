'''
https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        runProdFromRight = [1]
        for i in range(len(nums)-1):
            n = nums[i]
            runProdFromRight.append(runProdFromRight[-1] * n)
        
        output = []

        runProdFromLeft = 1
        for i in range(len(nums)-1, -1, -1):
            output.insert(0, runProdFromLeft * runProdFromRight[i])
            runProdFromLeft *= nums[i]
        
        return output
    
    def test(self):
        cases = [
            dict(nums=[1,2,3,4], output=[24,12,8,6])
        ]

        for c in cases:
            res = self.productExceptSelf(c["nums"])
            print("case: ", c["nums"])
            print("res: ", res)
            assert res == c["output"]

sol = Solution()
sol.test()
