class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head == None:
            return False

        idSet = set()

        n = head
        while n != None:
            
            nid = id(n)

            if nid in idSet:
                return True
            else:
                idSet.add(nid)

            n = n.next
        
        return False