# https://leetcode.com/problems/insert-interval/

class Solution:
    ''' 
    Time complexity: O(n) where n ~ len(intervals)
    Space complexity: O(1) since the only piece of new information being added is the new interval itself.
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # check if intervals is already empty, if it is, then just add the new interval and return the intervals
        if not intervals:
            intervals.append(newInterval)
            return intervals

        newStart, newEnd = newInterval[0], newInterval[1]

        if intervals[-1][1] < newStart:
            intervals.append(newInterval)
            return intervals

        # Step 1: Find where to insert new interval based on starting points
        i = 0
        while i < len(intervals):
            currInterval = intervals[i]
            currStart, currEnd = currInterval[0], currInterval[1]

            if currStart <= newStart and newStart <= currEnd:
                intervals.insert(i+1, newInterval)
                break
            elif newStart <= currStart:
                intervals.insert(i, newInterval)
                break
            i += 1
        
        # Step 2: resolve overlaps that new interval may cause
        while i < len(intervals)-1:
            currInterval = intervals[i]
            nextInterval = intervals[i+1]

            if currInterval[1] >= nextInterval[0] and currInterval[1] >= nextInterval[1]:
                # if the current interval is completely above the next interval
                intervals.pop(i+1)
                i -= 1
            elif currInterval[1] >= nextInterval[0]:
                # if the current interval intersects into the next interval
                currInterval[1] = nextInterval[1]
                i -= 1
            i += 1
        
        return intervals
    
    def test(self):
        cases = [
            dict(intervals=[[1,3],[6,9]], newInterval=[2,5], expected=[[1,5],[6,9]]),
            dict(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8], expected=[[1,2],[3,10],[12,16]]),
            dict(intervals=[], newInterval=[2,5], expected=[[2,5]]),
            dict(intervals=[[1,5]], newInterval=[2,3], expected=[[1,5]])
        ]

        for case in cases:
            intervals = case["intervals"]
            newInterval = case["newInterval"]
            expected = case["expected"]

            print(f"Case: intervals:{intervals}, newInterval: {newInterval}")
            res = self.insert(intervals, newInterval)
            print("result: ", res)
            assert res == expected

sol = Solution()
sol.test()
