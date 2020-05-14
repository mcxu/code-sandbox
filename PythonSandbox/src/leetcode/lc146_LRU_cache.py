'''
https://leetcode.com/problems/lru-cache/
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity. 
Follow up: Could you do both operations in O(1) time complexity?
'''
import time
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {} # maps: key to node
        self.head = None # least recently used
        self.tail = None # most recently used

    def get(self, key: int) -> int:
        print("--- get: {}".format(key))
        if key not in self.nodeMap.keys():
            return -1
        result = self.nodeMap[key]
        # move result to the tail (most recently used)
        if result == self.head:
            self.tail.next = result
            self.head = self.head.next
            result.next.prev = result.prev
            result.next = None
            result.prev = self.tail
            self.tail = result
        elif result != self.tail:
            self.tail.next = result
            result.prev.next = result.next
            result.next.prev = result.prev
            result.next = None
            result.prev = self.tail
            self.tail = result
        #self.printlist()
        
        return result.value

    def put(self, key: int, value: int) -> None:
        print("--- put: {}:{}".format(key,value))
        
        n = Node(key, value)
        if self.head == None:
            self.head = n
            self.tail = self.head
            self.nodeMap[key] = n
        else:
            #self.printlist()
            if key not in self.nodeMap.keys():
                self.tail.next = n
                n.prev = self.tail
                self.tail = n
                self.nodeMap[key] = n
            else:
                if self.nodeMap[key] == self.head:
                    print("self.nodeMap[key] == self.head")
                    # remove the current head, set next to new head
                    if self.head != self.tail:
                        extnode = self.nodeMap[key]
                        self.head = self.head.next
                        extnode.next = None
                        self.head.prev = None
                        
                        # append new node as tail
                        self.tail.next = n
                        n.prev = self.tail
                        self.tail = n
                        self.nodeMap[key] = n
                    else:
                        self.head = n
                        self.tail = n
                        self.nodeMap[key] = n

                elif self.nodeMap[key] != self.tail:
                    print("self.nodeMap[key] != self.tail")
                    # remove existing node
                    extnode = self.nodeMap[key]
                    extnode.prev.next = extnode.next
                    extnode.next.prev = extnode.prev
                    extnode.next, extnode.prev = None, None
                    del extnode

                    # append new node as tail
                    self.tail.next = n
                    n.prev = self.tail
                    self.tail = n
                    self.nodeMap[key] = n
                else:
                    # if nodemap[key] is the tail
                    print("nodemap[key] is the tail. key={}, value={}".format(key,value))

                    # node becomes the new tail
                    if self.tail != self.head:
                        prev = self.tail.prev
                        self.tail.prev = None
                        prev.next = n
                        n.prev = prev
                        self.tail = n
                        self.nodeMap[key] = n
                    else:
                        self.head = n
                        self.tail = n
                        self.nodeMap[key] = n

        while len(self.nodeMap) > self.capacity:
            tmp = self.head
            self.head = self.head.next
            self.nodeMap.pop(tmp.key)
            #print("removing key: {} from nodemap".format(tmp.key))
            # completely detaching the old head fixed the printlist backwards memory leak
            tmp.next = None 
            self.head.prev = None
            del tmp

        self.printlist()

    # for debugging
    def printlist(self):
        print("printlist")
        n = self.head
        while n != None:
            print("     -> key: {}, value: {}".format(n.key, n.value))
            n = n.next
            #time.sleep(1)
        print(" backwards")
        n = self.tail
        while n != None:
            print("     <- key: {}, value: {}".format(n.key, n.value))
            n = n.prev
            #time.sleep(1)
        print(" head kv: {}:{}".format(self.head.key, self.head.value))
        print(" tail kv: {}:{}".format(self.tail.key, self.tail.value))
        print(" nodeMap: ")
        for key in self.nodeMap.keys():
            print(  "   key: {}, node value: {}".format(key, self.nodeMap[key].value))

def testPut():
    cache = LRUCache(2)
    cache.put(1,2)
    cache.put(3,4)
    cache.put(5,7)
    cache.put(3,5)
    cache.printlist()

def testGet():
    cache = LRUCache(2)
    cache.put(1,2)
    cache.put(3,4)
    cache.put(5,7)
    cache.put(3,5)
    cache.printlist()
    g1 = cache.get(5)
    print("g1: ", g1)

def test1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    get1 = cache.get(1)       # returns 1
    print("get1: ", get1)
    cache.put(3, 3);    # evicts key 2
    get2 = cache.get(2);       # returns -1 (not found)
    print("get2: ", get2)
    cache.put(4, 4);    # evicts key 1
    get1again = cache.get(1);       # returns -1 (not found)
    print("get1again: ", get1again)
    cache.get(3);       # returns 3
    cache.get(4);       # returns 4

def test2():
    # expected: [null,-1,null,-1,null,null,2,6]
    cache = LRUCache(2)
    g1 = cache.get(2)
    print("g1: ", g1)
    cache.put(2,6)
    g2 = cache.get(1)
    print("g2: ", g2)
    cache.put(1,5)
    cache.put(1,2)
    g3 = cache.get(1)
    print("g3: ", g3)
    g4 = cache.get(2)
    print("g4: ", g4)

def test3():
    cache = LRUCache(3)
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.get(2)
    cache.put(2,4)
    cache.put(5,5)
    cache.put(5,30)
    cache.get(5)
    cache.put(5,2)

def test4():
    actions= ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    inputs = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    cache = LRUCache(inputs[0][0])
    for i in range(1, len(actions)):
        action = actions[i]
        input = inputs[i]
        if action == "put":
            cache.put(input[0], input[1])
        elif action == "get":
            g = cache.get(input[0])
            print("gotten g: ", g)


#testPut()
#testGet()
#test1()
#test2()
#test3()
test4()