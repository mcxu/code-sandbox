# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals
        
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            if start <= newInterval[0] <= end:
                intervals.insert(i+1, newInterval)
                break
            elif newInterval[0] <= start and newInterval[0] <= end:
                intervals.insert(i, newInterval)
                break
            elif i == len(intervals)-1:
                intervals.append(newInterval)
                break
            i += 1
        
        # resolve overlaps that new interval may cause
        i = 0
        while i < len(intervals)-1:
            curr = intervals[i]
            nxt = intervals[i+1]
            if curr[1] >= nxt[0] and curr[1] >= nxt[1]:
                intervals.pop(i+1)
                i -= 1
            elif curr[1] >= nxt[0]:
                intervals[i][1] = nxt[1]
                intervals.pop(i+1)
                i -= 1
            i += 1
        
        return intervals