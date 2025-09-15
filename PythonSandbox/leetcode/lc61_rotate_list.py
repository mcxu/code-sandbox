'''
https://leetcode.com/problems/rotate-list/
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return head
        mod = k
        listLen = 1
        ki = 0
        while ki < mod:
            #print("mod: ", mod)
            #print("ki: ", ki)
            n = head
            prev=None
            while n.next != None:
                prev=n
                n=n.next
                if ki == 0:
                    listLen += 1
            #print("listLen: ", listLen)
            if ki == 0 and k > listLen:
                if k%listLen > 0:
                    mod = k%listLen
                #print("mod updated to: ", mod)
            if prev!=None: 
                prev.next=None
            else:
                break
            n.next=head
            head=n
            
            ki += 1
        
        return head