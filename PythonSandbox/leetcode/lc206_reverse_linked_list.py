'''
https://leetcode.com/problems/reverse-linked-list/
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def add(self, x):
        self.next = ListNode(x)
        return self.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head = prev
        return head
    
    def test1(self):
        head = ListNode(1)
        head.add(2).add(3).add(4).add(5)
        rl = self.reverseList(head)
        while rl != None:
            print("test1 rl val: ", rl.val)
            rl = rl.next

sol = Solution()
sol.test1()
