'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        
        if n1 == None:
            return n2
        elif n2 == None:
            return n1
        
        newHead = None
        if n1.val <= n2.val:
            newHead = n1
            n1 = n1.next
        else:
            newHead = n2
            n2 = n2.next
        
        n3 = newHead
        while n1 != None and n2 != None:
            if n1.val <= n2.val:
                n3.next = n1
                n1 = n1.next
            else:
                n3.next = n2
                n2 = n2.next
            n3 = n3.next
            
        if n1 == None:
            n3.next = n2
        elif n2 == None:
            n3.next = n1
        
        return newHead