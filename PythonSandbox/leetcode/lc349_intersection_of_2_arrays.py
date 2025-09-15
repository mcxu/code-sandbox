'''
https://leetcode.com/problems/intersection-of-two-arrays/
'''
class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        n1Set = set(nums1)
        out = set()
        for i,n in enumerate(nums2):
            if n in n1Set and n not in out:
                out.add(n)
        return list(out)