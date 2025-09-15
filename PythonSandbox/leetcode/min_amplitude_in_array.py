'''
https://leetcode.com/discuss/interview-question/553399/Google-or-OA-2020-or-Min-Amplitude-and-Ways-to-Split-String/484500

Question 1:
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. 
Amplitude is the range of the array (basically difference between largest and smallest element).

Example 1:
Input: [-1, 3, -1, 8, 5, 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

Example 2:
Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10
'''
class Solution:
    # TODO: Not correct
    def minAmplitude(self, arr):
        # find mean, O(n) time
        mean = sum(arr)/len(arr)
        print("mean: ", mean)
        diffArr = [] # diffs from mean
        for i,v in enumerate(arr):
            diffArr.append([abs(v-mean), i])
        
        diffArr = sorted(diffArr, key=lambda x: x[0]) #O(nlogn) time
    
        end = len(diffArr)-1
        for j in range(end, end-3, -1):
            idx = diffArr[j][1]
            arr[idx] = mean
        print("arr final: ", arr)
        return max(arr)-min(arr)
    
    def test1(self):
        #arr = [-1, 3, -1, 8, 5, 4] # expected: 2
        arr = [10, 10, 3, 4, 10] # expected: 0
        res = self.minAmplitude(arr)
        print("res: ", res)

sol = Solution()
sol.test1()

