'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    '''
    Let n = len(nums)
    Time: O(n): single for loop.
    Space: O(1): 2 pointers i and j.
    '''
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        
        i = 0
        for j in range(1, len(nums)):
            print("i={}, j={}, nums: {}".format(i,j,nums))
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        
        for _ in range(i+1,len(nums)):
            nums.pop()
        print("nums final: ", nums)
        return len(nums)


    '''
    This results in TLE.
    Let n = len(nums)
    Time: O(n^2)
    Space: O(1)
    '''
    def removeDuplicates2(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return 1

        i = 1
        # do shifts
        while i < len(nums):
            if nums[i] == nums[i-1]:
                self.shiftLeftBy1(nums, i)
                nums.pop()
            else:
                i+=1
        #print("nums after: ", nums)
        return len(nums)
    
    # k = left most index that you want to shift by 1
    def shiftLeftBy1(self, nums, k):
        while k < len(nums):
            nums[k-1] = nums[k]
            k += 1

    def test1(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        res = self.removeDuplicates(nums)
        print("test1 res: ", res)

prob = Solution()
prob.test1()