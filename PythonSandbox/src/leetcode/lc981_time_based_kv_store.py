'''
https://leetcode.com/problems/time-based-key-value-store/
'''
import heapq

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tsMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tsMap.keys():
            heapq.heappush(self.tsMap[key], (-timestamp, value))
        else:
            self.tsMap[key] = [(-timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        for tup in self.tsMap[key]:
            if -tup[0] <= timestamp:
                return tup[1] 
        return ""