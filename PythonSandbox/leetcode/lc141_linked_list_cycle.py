class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    """
    Use set to keeptrack of seen nodes.
    Time complexity: O(n), where n ~ length of linked list
    Space complexity: O(n)
    """
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


    """
    Use slow (node+1) and fast (node+2) pointer.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def hasCycle2Pointer(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow != None:
            slow = slow.next

            for _ in range(2):
                fast = fast.next
                if fast == None:
                    return False

            if slow == fast:
                return True
        
        return False