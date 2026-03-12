from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        for _,interval in enumerate(intervals):
            if not merged:
                merged.append(interval)
                continue
            
            lastInterval = merged[-1]
            if lastInterval[1] < interval[0]:
                merged.append(interval)
            elif interval[0] <= lastInterval[1] < interval[1]:
                lastInterval[1] = interval[1]

        return merged
    
    def test1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        result = self.merge(intervals)
        print("result: ", result)
        assert result == expected
    
    def test2(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        result = self.merge(intervals)
        print("result: ", result)
        assert result == expected
    
    def test3(self):
        intervals = [[4,7],[1,4]]
        expected = [[1,7]]
        result = self.merge(intervals)
        print("result: ", result)
        assert result == expected

if __name__ == "__main__":
    s = Solution()
    s.test1()
    # s.test2()
    # s.test3()
