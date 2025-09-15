import heapq
import ctypes

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heapArr = [] # stores tuples of (key, value)
        self.kvMap = {} # stores: key : memory addr of element in heapArr

    def get(self, key: int) -> int:
        if key in self.kvMap:
            addr = self.kvMap[key]
            tup_pyobject = ctypes.cast(addr, ctypes.py_object)
            return tup_pyobject.value[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kvMap:
            addr = self.kvMap[key]
            tup_pyobject = ctypes.cast(addr, ctypes.py_object)
            tup_pyobject = (key, value)
        else:
            if len(self.heapArr) > self.capacity:
                smallestTup = heapq.heappop(self.heapArr)
                if smallestTup[0] in self.kvMap:
                    self.kvMap.pop(smallestTup[0])

            newTup = (key,value)
            heapq.heappush(self.heapArr, newTup)
            self.kvMap[key] = id(newTup)