# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Merge2SortedLists:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        n1 = list1; n2 = list2
        mergedList = ListNode(-1000)
        n3 = mergedList

        while n1 != None and n2 != None:
            if n1.val == n2.val:
                n3.next = ListNode(n1.val); n3 = n3.next
                n3.next = ListNode(n2.val); n3 = n3.next
                n1 = n1.next
                n2 = n2.next
            elif n1.val > n2.val:
                n3.next = ListNode(n2.val); n3 = n3.next
                n2 = n2.next
            elif n1.val < n2.val:
                n3.next = ListNode(n1.val); n3 = n3.next
                n1 = n1.next
        
        #print("n1 ptr: ", n1.val if n1 else n1)
        #print("n2 ptr: ", n2.val if n2 else n2)

        if n1:
            n3.next = n1
        if n2:
            n3.next = n2

        return mergedList.next

    
    def printList(self, description, head):
        vals = []
        n = head
        while n != None:
            vals.append(n.val)
            n = n.next
        descStr = description if description else "VALS:"
        print(f"{descStr}",vals)
    
    def buildLinkedList(self, lst: [int]):
        if not lst:
            return None
        head = ListNode(lst[0])
        n = head
        for i in range(1, len(lst)):
            n.next = ListNode(lst[i])
            n = n.next
        return head


    def test1(self):
        #list1 = [1,2,4]; list2 = [1,3,4]
        list1 = []; list2 = [0]

        list1LL = self.buildLinkedList(list1)
        self.printList("list1: ", list1LL)
        list2LL = self.buildLinkedList(list2)
        self.printList("list2: ", list2LL)
        
        ml = self.mergeTwoLists(list1LL, list2LL)
        self.printList("merged: ", ml)

if __name__ == "__main__":
    c = Merge2SortedLists()
    c.test1()
    