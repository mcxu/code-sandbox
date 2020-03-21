'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

Deep copy a linked list where each node has a random pointer.
'''

class Node:
    def __init__(self, x:int, next:'Node'=None, random:'Node'=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head == None:
            return None
        
        # map to keep track of random pointers
        # format: old node to new node
        rpMap = {}
        
        # create new nodes with corresponding values
        n = head
        while n != None:
            newNode = Node(n.val)
            rpMap[n] = newNode
            n = n.next
    
        # create connections in new tree
        n = head
        while n != None:
            newNode = rpMap[n]
            
            if n.next != None:
                newNode.next = rpMap[n.next]
            if n.random != None:
                newNode.random = rpMap[n.random]
                
            n = n.next
        
        return rpMap[head]
    
    def test1(self):
        head = Node(7)
        b = Node(13)
        c = Node(11)
        d = Node(10)
        e = Node(1)
        
        head.next = b
        b.next = c
        c.next = d
        d.next = e
        
        head.random = e.next
        b.random = head
        c.random = e
        d.random = c
        e.random = head
        
        copied = self.copyRandomList(head)
        while copied != None:
            print("test1 copied val: {}, random val: {}".format(copied.val, copied.random if copied.random == None else copied.random.val))
            copied = copied.next

sol = Solution()
sol.test1()