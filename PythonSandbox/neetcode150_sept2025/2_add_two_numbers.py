class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        n1 = self.add_list(l1)
        n2 = self.add_list(l2)
        
        s = n1 + n2

        if s == "":
            return None

        srev = str(s)[::-1]

        # build output list
        head = ListNode(int(srev[0]))
        n = head
        for _, digit_str in enumerate(srev[1:]):
            n.next = ListNode(int(digit_str))
            n = n.next
        return head

    def add_list(self, ll) -> int:
        s = ""
        node = ll
        while node != None:
            s = str(node.val) + s
            node = node.next
        return int(s)