from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        prev = None
        curr = head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head = prev
        return head


    def buildList(self, head):
        if head == None:
            return head

        headNode = ListNode(head[0])
        currNode = headNode
        for i in range(1, len(head)):
            currVal = head[i]
            currNode.next = ListNode(currVal)
            currNode = currNode.next
        return headNode
    
    def listToArray(self, listNode: ListNode):
        valArray = []
        n = listNode
        while n != None:
            valArray.append(n.val)
            n = n.next    
        return valArray
    
    def test1(self):
        head = [1,2,3,4,5]
        headNode = self.buildList(head)
        valArray = self.listToArray(headNode)
        print("valArray: ", valArray)



if __name__ == "__main__":
    c = ReverseLinkedList()
    c.test1()