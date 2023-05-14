"""
Count inversions in an array using a merge sort method.
Basically count how "unordered" an array is.
"""

class Solution:
    def countInversions(self, arr):
        mergedArr, totalCount = self.mergeSortAndCount(arr)
        print("mergedArr: ", mergedArr)
        return totalCount

    def mergeSortAndCount(self, arr):
        print("----- mergeSortAndCount: arr: ", arr)
        if len(arr) <= 1:
            return arr, 0

        leftSubarray, leftCount = self.mergeSortAndCount(arr[:len(arr)//2])
        rightSubarray, rightCount = self.mergeSortAndCount(arr[len(arr)//2:])

        # merge the 2 halves
        mergeCount = 0
        mergedArr = []
        i, j = 0, 0
        while i < len(leftSubarray) and j < len(rightSubarray):
            print(f"i:{i}, j:{j}")
            if leftSubarray[i] <= rightSubarray[j]: # already correct order
                mergedArr.append(leftSubarray[i])
                i += 1
            else:
                mergedArr.append(rightSubarray[j]) # fix inverted order
                j += 1
                mergeCount += len(leftSubarray)-i
                print("mergeCount: ", mergeCount)
        
        mergedArr += leftSubarray[i:]
        mergedArr += rightSubarray[j:]

        totalCount = leftCount + rightCount + mergeCount
        return mergedArr, totalCount

    def test(self):
        # arr = [4, 3, 2, 1] # expected = 6
        arr = [2, 1, 4, 3, 5] # expected = 2
        res = self.countInversions(arr)
        print("res: ", res)

s = Solution()
s.test()