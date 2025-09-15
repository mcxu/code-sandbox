'''
https://leetcode.com/problems/non-overlapping-intervals/description/
'''
class Solution:
    ''' 
    Time complexity: O(nlogn) due to the sorting at the beginning
    Space complexity: O(1) due to the maxEndSoFar storing a single number
    '''
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1]) # O(nlogn) time complexity
        numOverlaps = 0
        
        maxEndSoFar = -float('inf')
        for interval in intervals:
            currStart, currEnd = interval[0], interval[1]

            if currStart >= maxEndSoFar:
                maxEndSoFar = currEnd
            else:
                numOverlaps += 1

        return numOverlaps

    def test(self):
        cases = [
            dict(intervals=[[1,2],[2,3],[3,4],[1,3]], expected=1),
            dict(intervals=[[1,2],[1,2],[1,2]], expected=2),
            dict(intervals=[[1,2],[2,3]], expected=0),
            dict(intervals=[[1,2],[2,3],[3,4],[-100,-2],[5,7]], expected=0),
            dict(intervals=[[1,100], [1,11], [11,22], [2,12]], expected=2)
        ]

        for case in cases:
            intervals = case["intervals"]
            expected = case["expected"]

            print(f"Case: intervals:{intervals}")
            res = self.eraseOverlapIntervals(intervals)
            print("result: ", res)
            assert res == expected

sol = Solution()
sol.test()