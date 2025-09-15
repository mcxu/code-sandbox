'''
Kth smallest number from 2 sorted arrays without merging them.
'''

class Solution:
    def kthSmallest(self, arr1, arr2, k):
        if k > len(arr1)+len(arr2):
            return 0
        i = 0
        j = 0
        c = 0
        v = None
        while i<len(arr1) and j<len(arr2):
            c += 1

            if arr1[i] < arr2[j]:
                v = arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                v = arr2[j]
                j += 1
            else:
                v = arr1[i]
                i += 1
            
            if c == k:
                return v

        if c < k:
            if i < len(arr1):
                return arr1[i+(k-c-1)]
            elif j < len(arr2):
                return arr2[j+(k-c-1)]
        return v
    
    def test1(self):
        arr1 = [1,2,3]
        arr2 = [2,4,6,7,9]
        #k = 7
        k = 9
        res = self.kthSmallest(arr1, arr2, k)
        print("res: ", res)

s=Solution()
s.test1()


                