# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: [[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i,curr in enumerate(intervals[:-1]):
            nxt = intervals[i+1]
            if nxt[0] < curr[1]:
                return False
        
        return True