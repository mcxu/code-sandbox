'''
https://leetcode.com/problems/meeting-rooms-ii/
https://www.lintcode.com/problem/919/description 
'''

import heapq

class Solution:
    # using heap
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if not intervals:
            return 0
            
        intervals = sorted(intervals, key=lambda x: x[0])
        print("intervals: ", intervals)
        endingTimeHeap = [intervals.pop(0)[1]]
        print("init heap: ", endingTimeHeap)

        for interval in intervals:
            print(f"--- curr interval: {interval}")
            currStart, currEnd = interval[0], interval[1]
            print("curr heap: ", endingTimeHeap)

            if currStart >= endingTimeHeap[0]:
                heapq.heappop(endingTimeHeap)
                print("heap popped: ", endingTimeHeap)
            
            heapq.heappush(endingTimeHeap, currEnd)
            print("heap pushed: ", endingTimeHeap)
        
        return len(endingTimeHeap)

    # using greedy
    def minMeetingRooms2(self, intervals) -> int:
        intervals = sorted(intervals, key=lambda x: x[1]) 

        meetingRooms = 1
        maxEndSoFar = -float('inf')
        for interval in intervals:
            currStart, currEnd = interval[0], interval[1]

            if currStart >= maxEndSoFar:
                maxEndSoFar = currEnd
            else:
                meetingRooms += 1

        return meetingRooms

    def test(self):
        cases = [
            #dict(intervals=[(0,30),(5,10),(15,20)], expected=2),
            #dict(intervals=[(2,7)], expected=1)
        ]

        for case in cases:
            intervals = case["intervals"]
            expected = case["expected"]

            print(f"Case: intervals:{intervals}")
            res = self.minMeetingRooms2(intervals)
            print("result: ", res)
            assert res == expected

sol = Solution()
sol.test()