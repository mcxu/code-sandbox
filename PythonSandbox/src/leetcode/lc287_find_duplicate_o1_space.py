'''
https://leetcode.com/problems/find-the-duplicate-number/
'''

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        for i,n in enumerate(nums):
            if nums[abs(n)] < 0:
                return abs(n)
            else:
                nums[abs(n)] = -1*nums[abs(n)]
        return 0

    def test1(self):
        #arr = [2,4,3,1,1]
        #arr = [2,3,2,3]
        #arr = [1,3,4,6,8,5,9,2,1,7]
        arr = [2,3,4,1,8,5,9,6,2,7]
        res = self.findDuplicate(arr)
        print("res: ", res)

s = Solution()
s.test1()