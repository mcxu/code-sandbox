'''
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers, find the length of the 
longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
'''

import heapq
from typing import List

class Solution2:
    """ Using a heap
    n ~ len(nums)
    Time complexity: O(n), while loop takes O(n) time. heapify takes O(n) time complexity.
    Space complexity: heap stores max n items
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        heapq.heapify(nums) # heapify time complexity: O(n)

        maxSeqLen = 1
        currSeq = 1

        while nums:
            currNum = heapq.heappop(nums) # heappop time complexity: O(1)
            #print("curNum: ", currNum, "    currSeq: ", currSeq, "   maxSeqLen:", maxSeqLen)
            
            if not nums:
                return maxSeqLen
            
            nextNum = nums[0]

            if currNum + 1 == nextNum:
                currSeq += 1
            elif currNum + 1 < nextNum:
                currSeq = 1
            
            maxSeqLen = max(maxSeqLen, currSeq)
        
        return maxSeqLen


class Solution:
    """ Using DFS
    define n ~ len(nums)
    Time complexity: O(n). For loop runs n times. DFS loops at most n times in while loop.
    Space complexity: O(n). numSet is O(n). DFS puts at most O(n) items on stack.
    """
    def longestConsecutive(self, nums: [int]) -> int:
        numSet = set(nums)
        visited = set()
        longestLen = 0
        for n in nums:
            count = self.dfs(n, numSet, visited)
            longestLen = max(longestLen, count)
        return longestLen

    def dfs(self, n, numSet, visited):
        stack = [n]
        count = 0
        while stack:
            currNum = stack.pop(-1)

            if currNum not in visited:
                visited.add(currNum)

                count += 1

                if currNum-1 in numSet:
                    stack.append(currNum-1)
                if currNum+1 in numSet:
                    stack.append(currNum+1)
        return count

    # initial attempt: time limit exceeded
    def longestConsecutive_old(self, nums) -> int:
        if not nums:
            return 0

        maxNum = max(nums)  # O(n) time
        minNum = min(nums)  # O(n) time
        aux = [0 for _ in range(maxNum-minNum+1)]
        if minNum >= 0:
            aux = [0 for _ in range(maxNum+1)]
            minNum = 0

        # populate aux
        for i in range(len(nums)):  # O(n) time
            biasedInd = nums[i]  # biasedInd could be negative
            ind = biasedInd + abs(minNum)
            aux[ind] = 1
        #print("aux: ", aux)

        count = 0
        maxCount = 0
        for j in range(len(aux)):
            if aux[j] == 1:
                count += aux[j]

            if aux[j] == 0 or j == len(aux)-1:
                if count > maxCount:
                    maxCount = count
                count = 0

        return maxCount

    def test1(self, alg):
        input = [100, 4, 200, 1, 3, 2]
        res = alg(input)
        print("test1 res: ", res)

    def test2(self, alg):
        input = [100, 4, 200, 1, 3, 2, 101, 54,
                 67, 68, 102, 301, 103, 23, 7, 104, 18]
        # should be 5 (100, 101, 102, 103, 104)
        res = alg(input)
        print("test1 res: ", res)

    def test3(self, alg):
        input = []
        #input = [0]
        #input = [0,0]
        res = alg(input)
        print("test3 res: ", res)

    def test4(self, alg):
        input = [-7, -6, -5, -4, -2, -1, 0, 1, 3, 5]
        res = alg(input)
        print("test4 res: ", res)

    def test5(self, alg):
        #input = [2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]
        input = [9000, 8999, 8998, 8997, 8996, 8995, 8994, 8993, 8992, 8991, 8990, 8989, 8988, 8987, 8986,
                 8985, 8984, 8983, 8982, 8981, 8980, 8979, 8978, 8977, 8976, 8975, 8974, 8973, 8972, 8971, 8970]
        res = alg(input)
        print("test5 res: ", res)


s = Solution()
#alg = s.longestConsecutive
alg = s.longestConsecutive_old

# s.test1(alg)
# s.test2(alg)
# s.test3()
# s.test4(alg)
s.test5(alg)
