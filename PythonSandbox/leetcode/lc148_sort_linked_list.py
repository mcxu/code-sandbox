# https://leetcode.com/problems/sort-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeLists(left, right)
    
    def mergeLists(self, h1, h2):
        if h1 == None:
            return h2
        if h2 == None:
            return h1
        
        n1 = h1; n2 = h2
        mergedHead = None
        if n1.val <= n2.val:
            mergedHead = n1
            n1 = n1.next
        elif n1.val > n2.val:
            mergedHead = n2
            n2 = n2.next
        n3 = mergedHead
        while n1 != None and n2 != None:
            if n1.val <= n2.val:
                n3.next = n1
                n1 = n1.next
            elif n1.val > n2.val:
                n3.next = n2
                n2 = n2.next
            n3 = n3.next
        
        if n1 == None:
            n3.next = n2
        elif n2 == None:
            n3.next = n1
        return mergedHead
    
    def getMid(self, head):
        prev = None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev != None: 
            prev.next = None
        return slow