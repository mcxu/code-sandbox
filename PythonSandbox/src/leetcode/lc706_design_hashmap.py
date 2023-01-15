# https://leetcode.com/problems/design-hashmap/
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [-1 for _ in range(10)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key >= len(self.arr):
            self.arr += [-1 for _ in range(key-len(self.arr)+1)]
        self.arr[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key > len(self.arr)-1:
            return -1
        return self.arr[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key <= len(self.arr)-1:
            self.arr[key] = -1
