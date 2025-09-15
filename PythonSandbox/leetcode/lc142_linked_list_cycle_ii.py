'''
142. Linked List Cycle II [Medium]
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the 
position (0-indexed) in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

https://leetcode.com/problems/linked-list-cycle-ii/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return self.findCycleBeginNode(head, slow)
            
        return None
    
    def findCycleBeginNode(self, head, slow):
        n = head
        while n != slow:
            n = n.next
            slow = slow.next
        
        return slow

    def list1(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next = head.next
        return head
    
    def test1(self):
        head = self.list1()
        startCycleNode = self.detectCycle(head)
        print("startCycleNode: ", startCycleNode.val)

sol = Solution()
sol.test1()

        