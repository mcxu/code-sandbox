'''
https://leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            n1 = nums1[i]
            if nums2 and n1 >= nums2[0]:
                # shift numbers to the right starting from i
                for j in range(len(nums1)-1, i, -1):
                    nums1[j] = nums1[j-1]
                nums1[i] = nums2.pop(0)
        
        while nums2:
            nums1[len(nums1)-len(nums2)-1] = nums2.pop(0)