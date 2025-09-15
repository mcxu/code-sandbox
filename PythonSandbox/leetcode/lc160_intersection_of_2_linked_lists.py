'''
LC160: https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        crossRef = set()
        n = headA
        while n != None:
            crossRef.add(id(n))
            n = n.next
        
        n = headB
        while n != None:
            if id(n) in crossRef:
                return n
            n = n.next
        return n