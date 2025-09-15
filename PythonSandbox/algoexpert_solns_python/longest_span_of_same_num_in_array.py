'''
Given array of integers, return the length of the longest
span of the same number.
'''
class Solution:
    def countLongest(self, arr):
        maxFlat = 1
        currFlat = 1
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                currFlat += 1
            else:
                currFlat = 1

            if currFlat > maxFlat:
                maxFlat = currFlat
        return maxFlat

sol = Solution()
#arr = [1,1,2,2,2,2,3,3]
#arr = [1,1,1,2,2,2,2]
#arr = [1,2,1]
arr = [2,2,1]
res = sol.countLongest(arr)
print("res: ", res)
