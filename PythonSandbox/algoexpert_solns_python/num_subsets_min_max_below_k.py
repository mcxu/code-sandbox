'''
https://leetcode.com/discuss/interview-question/268604/Google-interview-Number-of-subsets
Requirement: O(n^2) time or better.

Example 1:
nums = [2, 4, 5, 7]
k = 8
Output: 5
Explanation: [2], [4], [2, 4], [2, 4, 5], [2, 5]

Example 2:
nums = [1, 4, 3, 2]
k = 8
Output: 15
Explanation: 16 (2^4) - 1 (empty set) = 15

Example 3:
nums = [2, 4, 2, 5, 7]
k = 10
Output: 27
Explanation: 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27
'''

class Solution:
    def numSubsetsMinMaxBelowK(self, nums, k):
        nums = sorted(nums) # O(n*log(n)) time

        