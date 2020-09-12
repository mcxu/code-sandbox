'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import time
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        i = 1
        j = 1 # keep track of k nodes behind
        jNode = head
        jPrev = None
        
        n = head
        while n != None:
            # print("----- j:{}, jPrev:{}, jNode:{}, i:{}, n:{}".format(j, 
            #                                                     jPrev.val if jPrev is not None else None, 
            #                                                     jNode.val if jNode is not None else None, 
            #                                                     i, 
            #                                                     n.val if n is not None else None))
            if i % k == 0 and k > 1:
                ret = self.swapNodes(head, jPrev, jNode, n)
                head = ret[0]
                jPrev = ret[1]
                jNode = ret[1].next
                n = ret[1]
                j = i+1
            
            i += 1
            n=n.next

        return head
    
    def swapNodes(self, head, jPrev, jNode, iNode):
        #print("swapNodes")
        prev = jNode
        curr = jNode.next

        # change outer bound pointers
        if jPrev != None:
            jPrev.next = iNode
        jNode.next = iNode.next

        # print("prev: ", prev.val if prev is not None else None)
        # print("curr: ", curr.val if curr is not None else None)
        #print("nxt: ", nxt.val if nxt is not None else None)
        while curr != iNode and curr.next != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr.next = prev
        # print("curr next: ", curr.next.val)
        if jNode == head:
            head = curr
        #print("head: ", head.val)
        return [head, jNode, iNode]

    def test1(self):
        head = ListNode(1)
        vals = [2,3,4,5]
        n = head
        for v in vals:
            n.next = ListNode(v)
            n = n.next
        
        k = 4
        res = self.reverseKGroup(head, k)
        n = res
        while n != None:
            print("n: ", n.val)
            n = n.next
            time.sleep(1)

s=Solution()
s.test1()