'''
https://leetcode.com/problems/merge-intervals/
'''
from typing import List

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals = sorted(intervals, key=lambda x: x[0]) # O(nlogn), n= len(intervals)
        i = 0
        while i < len(intervals)-1:
            currInterval = intervals[i]
            nxtInterval = intervals[i+1]
            
            if currInterval[1] >= nxtInterval[0] and currInterval[1] >= nxtInterval[1]:
                intervals.pop(i+1)
                i -= 1
            elif currInterval[1] >= nxtInterval[0]:
                currInterval[1] = nxtInterval[1]
                intervals.pop(i+1)
                i -= 1
            
            i += 1
        
        return intervals
    
    # using min and max functions
    def merge2(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        i = 0
        while i < len(intervals)-1:
            a = intervals[i] # current interval
            b = intervals[i+1] # next interval

            if b[0] <= a[1] <= b[1] or a[0] <= b[1] <= a[1]:
                a[0] = min(a[0], b[0])
                a[1] = max(a[1], b[1])
                intervals.pop(i+1) # remove the next interval
                i -= 1
            i += 1 
        
        return intervals


    def test(self):
        cases = [
            dict(intervals=[[1,3],[2,6],[8,10],[15,18]], expected=[[1,6],[8,10],[15,18]]),
            dict(intervals=[[1,4],[4,5]], expected=[[1,5]]),
            dict(intervals=[[1,4],[0,4]], expected=[[0,4]]),
            dict(intervals=[[1,4],[0,0]], expected=[[0,0],[1,4]]),
            dict(intervals=[[1,4],[0,1]], expected=[[0,4]]),
            dict(intervals=[[1,4],[1,4]], expected=[[1,4]]),
            dict(intervals=[[1,4],[2,3]], expected=[[1,4]])
        ]

        for case in cases:
            intervals = case["intervals"]
            expected = case["expected"]

            print(f"Case: intervals:{intervals}")
            res = self.merge2(intervals)
            print("result: ", res)
            assert res == expected


sol = Solution()
sol.test()
