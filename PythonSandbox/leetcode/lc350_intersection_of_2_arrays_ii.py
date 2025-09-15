'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        n1Freq = {}
        n2Freq = {}
        for i,n in enumerate(nums1):
            if n in n1Freq.keys():
                n1Freq[n] += 1
            else:
                n1Freq[n] = 1
        
        for i,n in enumerate(nums2):
            if n in n2Freq.keys():
                n2Freq[n] += 1
            else:
                n2Freq[n] = 1
        
        chosenMap = n1Freq
        otherMap = n2Freq
        if len(n1Freq) >= len(n2Freq):
            chosenMap = n2Freq
            otherMap = n1Freq
        
        out = []
        for k in chosenMap.keys():
            if k in otherMap.keys():
                out += ([k] * min(chosenMap[k],otherMap[k]))
        return out

    def intersectPresorted(self, nums1: [int], nums2: [int]) -> [int]:
        i = 0; j = 0
        out = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i]==nums2[j]:
                out.append(nums1[i])
                i+=1; j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
        return out
    
    def test_intersectPresorted1(self):
        nums1 = sorted([1,2,2,1])
        nums2 = [2,2]
        res = self.intersectPresorted(nums1, nums2)
        print("res: ", res)

    def test_intersectPresorted2(self):
        nums1 = sorted([4,9,5])
        nums2 = sorted([9,4,9,8,4])
        res = self.intersectPresorted(nums1, nums2)
        print("res: ", res)

    def test_intersectPresorted3(self):
        nums1 = sorted([4,9,5,1,3,5,7])
        nums2 = sorted([9,4,9,8,4,7,3,5,5])
        print("nums1 sorted: {}\nnums2 sorted: {}".format(nums1,nums2))
        res = self.intersectPresorted(nums1, nums2)
        print("res: ", res)

s = Solution()
#s.test_intersectPresorted1()
#s.test_intersectPresorted2()
s.test_intersectPresorted3()