'''
https://leetcode.com/problems/the-k-strongest-values-in-an-array/
Given an array of integers arr and an integer k.
A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| > |arr[j] - m| where m is the median of the array.
If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].
Return a list of the strongest k values in the array. return the answer in any arbitrary order.
'''
class Solution:
    def getStrongest(self, arr: [int], k: int) -> [int]:
        arr = sorted(arr)
        m = self.median(arr)
        strongest = []
        for n in range(k):
            i = 0
            j = len(arr)-1
            ival = arr[i]
            jval = arr[j]
            if abs(ival-m) > abs(jval-m):
                strongest.append(ival)
                arr.pop(i)
            else:
                strongest.append(jval)
                arr.pop(j)
        
        return strongest
        
    # arr must be sorted first
    def median(self, arr):
        return arr[int((len(arr)-1)/2)]

    def test1(self):
        arr = [6,7,11,7,6,8]
        k = 5
        res = self.getStrongest(arr, k)
        print("res: ", res)

s = Solution()
s.test1()