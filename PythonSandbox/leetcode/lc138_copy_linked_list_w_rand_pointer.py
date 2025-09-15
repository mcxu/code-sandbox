'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

Deep copy a linked list where each node has a random pointer.
'''
from pip._vendor.requests.api import head

class Node:
    def __init__(self, x:int, next:'Node'=None, random:'Node'=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    '''
    Uses a map to keep track of new nodes.
    Let n = number of nodes in the list to copy.
    Time complexity: O(n), since creating the new nodes is O(n) time, and setting all the pointers in the new nodes is O(n) time.
    Space complexity: O(n), since the nnMap stores up to n entries.
    '''
    def copyRandomList(self, head: Node) -> Node:
        if head == None:
            return head
        
        # new node map, to keep track of new nodes
        nnMap = {}
        
        # create new nodes with corresponding values, O(n) time
        n = head
        while n != None:
            nnMap[n] = Node(n.val)
            n = n.next
        print("nnNap: ", nnMap)
        # create connections in new tree, O(n) time
        n = head
        while n != None:
            newNode = nnMap[n]
            
            if n.next != None:
                newNode.next = nnMap[n.next]
            if n.random != None:
                newNode.random = nnMap[n.random]
                
            n = n.next
        
        return nnMap[head]
    
    '''
    Do a deep copy without using map.
    
    '''
    def copyRandomListWOMap(self, head:'Node') -> 'Node':
        if head == None:
            return head
        
        # create new node after each old node
        n = head
        while n != None:
            tmp = n.next
            n.next = Node(n.val)
            n.next.next = tmp
            n = tmp
        
#         print("print list:"); n = head
#         while n != None: print("n.val: ", n.val); n = n.next
        
        # set up the random pointers for each new node
        n = head
        while n != None:
            #print("B n.val: ", n.val)
            if n.random == None:
                n.next.random = n.random
            else:
                n.next.random  = n.random.next
            n = n.next.next
        
        # decouple the new nodes from old nodes
        n = head
        newHead = head.next
        newn = newHead
        while n.next != None or newn.next != None:
            tmp1 = n.next.next
            # condition to check for when n gets to the last of it's node,
            # which means that n.next.next = None
            if tmp1 == None:
                n.next = tmp1
                break
            tmp2 = newn.next.next
            n.next = tmp1
            newn.next = tmp2
            n = tmp1
            newn = tmp2
            
#         print("C checking old list:"); n = head
#         while n != None: print("C n.val: ", n.val); n = n.next
        return newHead
    
    def test1(self, alg):
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
        
        copied = alg(head)
        headAddr = hex(id(head))
        print("address of original list:   ", headAddr)
        copiedListAddr = hex(id(copied))
        print("address of copied list:     ", copiedListAddr)
        while copied != None:
            print("test1 copied val: {}, random val: {}".format(copied.val, copied.random if copied.random == None else copied.random.val))
            copied = copied.next

sol = Solution()
sol.test1(sol.copyRandomList)
#sol.test1(sol.copyRandomListWOMap)