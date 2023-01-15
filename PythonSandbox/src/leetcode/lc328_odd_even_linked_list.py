'''
LC328: https://leetcode.com/problems/odd-even-linked-list/
'''
import unittest
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        currOdd=head
        currEven=head.next
        evenHead=head.next
        prev = None
        while currOdd != None and currEven != None:
            # do odd
            prev=currOdd
            currOdd.next = currEven.next
            currOdd = currOdd.next
            if currOdd == None:
                prev.next = evenHead
                return head
                
            # do even
            currEven.next = currOdd.next
            currEven = currEven.next
            
        if currEven == None:
            currOdd.next = evenHead

        return head

class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def buildLinkedList(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        n = head
        for i in range(1, len(arr)):
            n.next = ListNode(arr[i])
            n = n.next
        return head
    
    def buildArray(self, head):
        arr = []
        n = head
        while n != None:
            arr.append(n.val)
            n = n.next
        return arr
    
    def printLinkedList(self, head):
        n = head
        while n != None:
            print("{} ->".format(n.val), end=" ")
            n = n.next
        print("None")

    def evalTest(self, arr, expected, testNum):
        ll = self.buildLinkedList(arr)
        result = self.sol.oddEvenList(ll)
        self.printLinkedList(result)
        resArr = self.buildArray(result)
        self.assertEqual(expected, resArr, msg="test_{} fail".format(testNum))

    def test_1(self):
        arr = [1,2,3,4,5]
        expected = [1,3,5,2,4]
        self.evalTest(arr, expected, 1)
    
    def test_2(self):
        arr = [2,1,3,5,6,4,7]
        expected = [2,3,6,7,1,5,4]
        self.evalTest(arr, expected, 2)

unittest.main()