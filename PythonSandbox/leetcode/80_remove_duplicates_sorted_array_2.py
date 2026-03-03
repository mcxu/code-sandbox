'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0
        
        c = 0
        i = 0
        ref = nums[i]
        while i < len(nums):
            curr = nums[i]
            if curr == ref:
                c+=1
            else:
                ref = nums[i]
                c = 1
            
            if c > 2:
                nums.pop(i)
                c -= 1
                i -= 1
            i += 1
        
        return len(nums)
    
    def test1(self):
        #nums = [1,1,1,2,2,3]
        nums = [0,0,1,1,1,1,2,3,3]
        #nums = [1,1,1,2,2,3]
        res = self.removeDuplicates(nums)
        print("test1 res: ", res)

prob = Solution()
prob.test1()