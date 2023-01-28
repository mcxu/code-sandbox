'''
https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        prodsFromLeft = [1]
        for i in range(0, len(nums)-1):
            prodsFromLeft.append(prodsFromLeft[-1]*nums[i])   
        
        latestProdFromRight = 1
        for i in range(len(nums)-1, -1, -1):
            prodsFromLeft[i] = prodsFromLeft[i] * latestProdFromRight
            latestProdFromRight = latestProdFromRight * nums[i]

        return prodsFromLeft
    
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