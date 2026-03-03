# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: [[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i,curr in enumerate(intervals[:-1]):
            nxt = intervals[i+1]
            if nxt[0] < curr[1]:
                return False
        
        return True

    def test(self):
        cases = [
            dict(intervals=[(0,30),(5,10),(15,20)], expected=False),
            dict(intervals=[(5,8),(9,15)], expected=True)
        ]

        for case in cases:
            intervals = case["intervals"]
            expected = case["expected"]

            print(f"Case: intervals:{intervals}")
            res = self.canAttendMeetings(intervals)
            print("result: ", res)
            assert res == expected

sol = Solution()
sol.test()