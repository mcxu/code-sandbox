# https://leetcode.com/problems/meeting-rooms-ii/

import heapq

class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if not intervals:
            return 0
            
        intervals = sorted(intervals, key=lambda x: x[0])
        print("intervals: ", intervals)
        endingTimeHeap = [intervals.pop(0)[1]]
        for i,n in enumerate(intervals):
            print("i={} n: {}".format(i,n))
            print("heap: ", endingTimeHeap)
            if n[0] >= endingTimeHeap[0]:
                heapq.heappop(endingTimeHeap)
            
            heapq.heappush(endingTimeHeap, n[1])
            print("heap end: ", endingTimeHeap)
        
        return len(endingTimeHeap)