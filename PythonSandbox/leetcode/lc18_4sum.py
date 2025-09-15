# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        quads = set()
        for i in range(len(nums)-3):
            self.helper(nums, target, i, i+1, i+2, len(nums)-1, quads)
        
        return quads
    
    def helper(self, nums, target, a, b, c, d, quads):
        if b>=c or c>=d:
            return
        
        aval=nums[a]; bval=nums[b]; cval=nums[c]; dval=nums[d]
        currQuad = (aval,bval,cval,dval)
        currSum = sum(currQuad)
        
        if currSum==target and currQuad not in quads:
            quads.add(currQuad)
        
        if currSum<target:
            self.helper(nums, target, a, b+1, c, d, quads)
            self.helper(nums, target, a, b, c+1, d, quads)
        else:
            self.helper(nums, target, a, b, c, d-1, quads)
    

    def test1(self):
        arr = [-2,6,3,1,-6,-2,9,-3,0,-7,8,-10,-4,9,1,1,-5,-9]
        target = 0
        res = self.fourSum(arr, target)
        print("res: ", res)

s = Solution()
s.test1()