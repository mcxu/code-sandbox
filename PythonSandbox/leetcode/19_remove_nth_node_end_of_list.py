
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeMap = {} # index : node
        i = 0
        m = head
        while m != None:
            nodeMap[i] = m
            if len(nodeMap) > n+1:
                nodeMap.pop(i-n-1)
            i += 1
            m = m.next
        
        # remove using map
        maxInd = max(nodeMap.keys())
        nthInd = maxInd-n+1
        if nthInd-1 >= 0:
            nodeMap[nthInd-1].next = nodeMap[nthInd].next
        
        if nodeMap[nthInd] == head:
            head = head.next
        nodeMap[nthInd].next = None
        nodeMap.pop(nthInd)
        
        return head