# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List, Callable
from collections import deque

class SlidingWindowMax:
    def maxSlidingWindow_bruteForce(self, nums: List[int], k: int) -> List[int]:
        maxValues = []
        maxIdx = self.findMaxIdx(nums, 0, k)

        # r = rightmost index of the sliding window
        for r in range(k-1, len(nums)):
            l = r-k+1
            # print(f"=== l:{l}, r:{r}, subarray: ", nums[l:r+1])
            # print("maxIdx: ", maxIdx, "   num at maxIdx: ", nums[maxIdx])

            # # if maxIdx still within prev window
            if maxIdx >= l:
                # compare the max number with the new number
                if nums[maxIdx] <= nums[r]:
                    maxIdx = r
            else:
                maxIdx = self.findMaxIdx(nums, l, r+1)
            
            maxValues.append(nums[maxIdx])

        return maxValues

    def findMaxIdx(self, nums, l, r): # l inclusive, r exclusive
        maxIdx = l
        maxNum = -float('inf')
        while l < r:
            print('in while, l: ', l)
            if nums[l] > maxNum:
                maxIdx = l
                maxNum = nums[maxIdx]
                print("new maxIdx: ", maxIdx, "   new max num: ", nums[maxIdx])
            l += 1
        return maxIdx


    def maxSlidingWindow_optimized(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # stores indices
        maxValues = []
        for i in range(len(nums)):
            print("--- i=", i, "   i val: ", nums[i], "   maxValues: ", maxValues)
            print("dq for loop top: ", dq)

            # Maintain Monotonicity (Remove smaller elements from the back, aka right side)
            # For the new element nums[i], remove all indices from the back of the deque 
            # whose corresponding elements are less than or equal to nums[i].
            # This ensures the deque remains monotonically decreasing (decreasing from right to left side)
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
                print("dq popped from back: ", dq)
            
            # Add current element index
            dq.append(i)
            print("dq appended: ", dq)

            # Remove Out-of-Window Elements (Remove from the front, aka left side)
            # The index at the front of the deque (q[0]) is the current window's max.
            # If this index is outside the current window (i.e., it's smaller than the 
            # start of the current window, which is i - k + 1), remove it.
            if dq[0] == i - k:
                dq.popleft()
                print("dq popped from front: ", dq)
            
            # Record the Maximum (Once the first full window is formed)
            # A full window of size k is formed when the index 'i' reaches k - 1.
            # For every index 'i' from k - 1 onwards, the current maximum is at q[0].
            if i >= k - 1:
                idxOfMaxValInWindow = dq[0]
                print("idxOfMaxValInWindow: ", idxOfMaxValInWindow)
                maxValues.append(nums[idxOfMaxValInWindow])
                print("maxValues appended: ", maxValues)
        
        return maxValues


    def test(self):
        FN_TO_TEST: Callable = self.maxSlidingWindow_optimized

        tests = [
            dict(nums=[1,3,-1,-3,5,3,6,7], k=3, expected=[3,3,5,5,6,7]),
            # dict(nums=[1,-1], k=1, expected=[1,-1]),
            # dict(nums=[-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7], k=7, expected=[9,9,10,10,10,10,10,10,10,9,9,9,8,8]),
            # dict(nums=[3,1,1,3], k=3, expected=[3,3]),
            # dict(nums=[1,3,1,2,0,5], k=3, expected=[3,3,2,5]),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["nums"], tc["k"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation


if __name__=="__main__":
    c = SlidingWindowMax()
    c.test()