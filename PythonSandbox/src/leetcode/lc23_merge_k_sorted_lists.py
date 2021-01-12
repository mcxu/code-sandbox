'''
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
import heapq

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    # using only priority queue
    def mergeKLists4(self, lists: [ListNode]) -> ListNode:
        heap = []
        for i,lst in enumerate(lists):
            n = lst
            while n != None:
                heapq.heappush(heap, n.val)
                n = n.next
        
        if not heap:
            return None
        
        mergedHead = ListNode(heapq.heappop(heap))
        m = mergedHead
        while heap:
            p = heapq.heappop(heap)
            m.next = ListNode(p)
            m = m.next
        
        return mergedHead
    
    # using priority queue and hashmap for frequency count
    def mergeKLists3(self, lists: [ListNode]) -> ListNode:
        freqMap = {}
        heap = []
        for i,lst in enumerate(lists):
            n = lst
            while n != None:
                if n.val not in freqMap.keys():
                    freqMap[n.val] = 1
                    heapq.heappush(heap, n.val)
                else:
                    freqMap[n.val] += 1
                n = n.next
        
        if not heap:
            return None
        
        heapRoot = heap[0]
        mergedHead = ListNode(heapRoot)
        m = mergedHead
        while heap:
            p = heapq.heappop(heap)
            lim = freqMap[p]
            if p==heapRoot:
                lim -= 1
            for i in range(lim):
                m.next = ListNode(p)
                m = m.next
        
        return mergedHead


    '''
    Let n = total number of elements in all k lists.
    Time: O(nlogn), since the worst complexity comes from the sort.
    Space: O(n), since values array stores n elements.
    '''
    def mergeKLists2(self, lists):
        # add vals to values array
        values = [] 
        for listHead in lists:
            n = listHead
            while n != None:
                values.append(n.val)
                n = n.next
        
        values = sorted(values) # O(nlogn) time
        
        mergedHead = None
        m = None
        for i in range(len(values)):
            if mergedHead == None:
                mergedHead = ListNode(values[i])
                m = mergedHead
            else:
                m.next = ListNode(values[i])
                m = m.next
        return mergedHead

    def test2(self):
        lists = [
            [1,4,5,100],
            [1,3,4],
            [7,13],
            [2,6,10,23,45,100]]
        listsLL = [self.createLLFromArray(x) for x in lists]
        res = self.mergeKLists2(listsLL)
        self.printLL(res)

    #====================================================================

    # Results in TLE
    def mergeKLists1(self, lists):
        if not lists:
            return None
        elif len(lists) < 2:
            return lists[0]
        elif len(lists) < 3:
            return self.merge2ListsWithPointers(lists[0], lists[1])
        
        mergedHead = self.merge2ListsWithPointers(lists[0], lists[1])
        for i in range(2, len(lists)):
            listHead = lists[i]
            mergedHead = self.merge2ListsWithPointers(mergedHead, listHead)
        return mergedHead

    def merge2ListsWithPointers(self, list1, list2):
        p1 = list1
        p2 = list2
        p1Prev = None
        p2Prev = None
        merged = None
        m = None # pointer for merged list
        while p1 != None and p2 != None:
            v1 = p1.val
            v2 = p2.val
            if v1 == v2:
                if merged == None:
                    merged = ListNode(v1)
                    merged.next = ListNode(v2)
                    m = merged.next
                else:
                    m.next = ListNode(v1)
                    m.next.next = ListNode(v2)
                    m = m.next.next
                p1Prev = p1
                p2Prev = p2
                p1 = p1.next
                p2 = p2.next
            elif v1 > v2:
                if merged == None:
                    merged = ListNode(v2)
                    m = merged
                else:
                    m.next = ListNode(v2)
                    m = m.next
                p2Prev = p2
                p2 = p2.next
            else:
                if merged == None:
                    merged = ListNode(v1)
                    m = merged
                else:
                    m.next = ListNode(v1)
                    m = m.next
                p1Prev = p1
                p1 = p1.next

        if p1 != None:
            if merged == None:
                merged = p1
            else:
                m.next = p1
                # prevent memory leak
                if p1Prev:
                    p1Prev.next = None

        if p2 != None:
            if merged == None:
                merged = p2
            else:
                m.next = p2
                # prevent memory leak
                if p2Prev:
                    p2Prev.next = None

        return merged

    def createLLFromArray(self, arr):
        head = ListNode(arr[0])
        n = head
        for i in range(1, len(arr)):
            n.next = ListNode(arr[i])
            n = n.next
        return head

    def printLL(self, head):
        print("printing LL beginning with: ", head.val)
        n = head
        while n != None:
            print("{} -> ".format(n.val), end="")
            n = n.next
        print("None")

    def testMerge2ListsWithPointers(self):
        list1 = [1,4,5]
        list2 = [1,3,4]
        ll1 = self.createLLFromArray(list1)
        self.printLL(ll1)
        ll2 = self.createLLFromArray(list2)
        self.printLL(ll2)
        m = self.merge2ListsWithPointers(ll1, ll2)
        self.printLL(m)
    
    def test1(self):
        lists = [
            [1,4,5,100],
            [1,3,4],
            [7,13],
            [2,6,10,23,45,100]]
        listsLL = [self.createLLFromArray(x) for x in lists]
        res = self.mergeKLists1(listsLL)
        self.printLL(res)

sol = Solution()
#sol.testMerge2ListsWithPointers()
#sol.test1()
#sol.test2()