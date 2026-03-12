from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        for _,(s,e) in enumerate(intervals):
            if not merged or merged[-1][1] < s:
                merged.append([s,e])
            elif s <= merged[-1][1] < e:
                merged[-1][1] = e

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
    # s.test1()
    # s.test2()
    s.test3()
