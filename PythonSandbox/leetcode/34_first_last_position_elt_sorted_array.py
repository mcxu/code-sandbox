'''
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
'''

class Solution:
    '''
    Let n = len(nums), m = number of instances of target value
    Time complexity: O(log2(n) + m), since the binary search is O(log2(n)) and the expansion is O(m)
    Space complexity: O(1), since the pointers that store information are loInd, medInd, highInd, and i,j in expand().
    '''
    def searchRange(self, nums, target):
        loInd = 0
        hiInd = len(nums)-1
        
        while loInd <= hiInd:
            medInd= int((loInd + hiInd)/2)
#             print("medInd: ", medInd)
#             print("target found: ", nums[medInd])
            
            if nums[loInd] == target:
                return self.expand(nums, target, loInd)
            elif nums[medInd] == target:
                return self.expand(nums, target, medInd)
            elif nums[hiInd] == target:
                return self.expand(nums, target, hiInd)
            
            if nums[medInd] < target:
                loInd = medInd+1
            else:
                hiInd = medInd-1
            
        return [-1, -1]
    
    def expand(self, nums, target, i):
        j = i
#         print("start of expand: i={}, j={}".format(i,j))
        while i >= 0 and nums[i] == target:
            i -= 1
        
        while j <= len(nums)-1 and nums[j] == target:
            j += 1
            
        return [i+1, j-1]
    
    def test1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        #Output: [3,4]
        res = self.searchRange(nums, target)
        print("test1 res: ", res)

    def test2(self):
#         nums = [1]
#         target = 1
#         nums = [2,2]
#         target = 2
        nums = [1,4]
        target = 4
        res = self.searchRange(nums, target)
        print("test2 res: ", res)
        
s = Solution()
s.test1()
#s.test2()