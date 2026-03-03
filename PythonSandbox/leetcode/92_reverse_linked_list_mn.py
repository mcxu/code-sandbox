'''
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def add(self, x):
        self.next = ListNode(x)
        return self.next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or m == n:
            return head
        
        i = 1
        prev = None
        curr = head
        while i < m:
            #print("i={}, prev: {}, curr: {}".format(i, None if prev==None else prev.val, None if curr==None else curr.val))
            if prev == None:
                prev = head
            else:
                prev = prev.next
            curr = curr.next
            i += 1
        
        #print("A i={}, prev: {}, curr: {}".format(i, None if prev==None else prev.val, None if curr==None else curr.val))
        
        # set the pointer for the m'th node and the pointer before it.
        mprev = prev
        mptr = curr
        
        #print("mprev: {}, mptr: {}".format(None if mprev==None else mprev.val, None if mptr==None else mptr.val))
        
        while i < n:
            next = curr.next
            #print("B i={}, prev: {}, curr: {}, next: {}".format(i, None if prev==None else prev.val, None if curr==None else curr.val, None if next==None else next.val))
            curr.next = prev
            #print("    curr.next set to: ", None if curr.next==None else curr.next.val)
            prev = curr
            curr = next
            i += 1
        
        next = curr.next
        #print("C i={}, prev: {}, curr: {}, next: {}".format(i, None if prev==None else prev.val, None if curr==None else curr.val, None if next==None else next.val))
        curr.next = prev
        #print("    curr.next set to: ", curr.next.val)
        #print("C mprev: {}, mptr: {}".format(None if mprev==None else mprev.val, None if mptr==None else mptr.val))
        
        mptr.next = next
        
        if mprev != None:   
            mprev.next = curr
        
        if m == 1:
            return curr
        
        return head
        
    def test1(self, alg):
        head = ListNode(1)
        head.add(2).add(3).add(4)
        m=2; n=3
        rev = self.reverseBetween(head, m, n)
        while rev != None:
            print("test1 rev val: ", rev.val)
            rev = rev.next
    
    def test2(self, alg):
        head = ListNode(1)
        head.add(2).add(3).add(4).add(5)
        m=2; n=4
        rev = self.reverseBetween(head, m, n)
        while rev != None:
            print("test2 rev val: ", rev.val)
            rev = rev.next
    
    def test3(self, alg):
        head = ListNode(5)
        m = 1
        n = 1
        rev = self.reverseBetween(head, m, n)
        while rev != None:
            print("test3 rev val: ", rev.val)
            rev = rev.next

    def test4(self, alg):
        head = ListNode(3); head.add(5)
        m = 1
        n = 2
        rev = self.reverseBetween(head, m, n)
        while rev != None:
            print("test4 rev val: ", rev.val)
            rev = rev.next
    
sol = Solution()
#sol.test1(sol.reverseBetween)
#sol.test2(sol.reverseBetween)
#sol.test3(sol.reverseBetween)
sol.test4(sol.reverseBetween)

