'''
https://leetcode.com/problems/merge-intervals/
'''
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