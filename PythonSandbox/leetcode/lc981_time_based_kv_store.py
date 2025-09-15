'''
https://leetcode.com/problems/time-based-key-value-store/
'''
import heapq

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyMap = {} # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(f"--- SET key: {key}, value: {value}, timestamp: {timestamp}")
        if key not in self.keyMap:
            self.keyMap[key] = [(timestamp, value)]
        else:
            self.keyMap[key].append((timestamp, value))
        # print("keymap: ", self.keyMap)

    def get(self, key: str, timestamp: int) -> str:
        # binary search since lists of (timestamp, value) have strictly increasing timestamp
        # print(f"--- GET key: {key}, timestamp: {timestamp}")
        if key in self.keyMap:

            if timestamp < self.keyMap[key][0][0]:
                return ""

            lo = 0
            hi = len(self.keyMap[key])

            while lo < hi:
                # print(f"lo: {lo}, hi: {hi}")
                midIdx = (lo + hi)//2
                midTup = self.keyMap[key][midIdx]

                if midTup[0] <= timestamp:
                    lo = midIdx + 1
                else:
                    hi = midIdx 

            return self.keyMap[key][lo-1][1]

        return ""

    def test(self):
        actions = ["TimeMap","set","get","get","set","get","get"]
        inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
        expected = [None,None,"bar","bar",None,"bar2","bar2"]

        tm = TimeMap()

        for i in range(1, len(actions)):
            action = actions[i]
            ip = inputs[i]
            if action == "set":
                tm.set(ip[0], ip[1], ip[2])
            elif action == "get":
                result = tm.get(ip[0], ip[1])
                if result == expected[i]:
                    print(f"Correct output for test case {action}: {ip} with result: {result} and expected: {expected[i]}")
                else:
                    print(f"Wrong output for test case {action}: {ip} with result: {result} and expected: {expected[i]}")

tm = TimeMap()
tm.test()


# old solution that used to pass, but doesn't anymore
class TimeMap_Old:

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
