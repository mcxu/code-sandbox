import unittest

class DLLNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.insertAfter(self.tail, node)
        
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert) # remove if already in list
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev == None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


    def insertAfter(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next == None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            k = self.head
            c = 1
            while k != None and c != position:
                c+=1
                k = k.next
            if k != None:
                self.insertBefore(k, nodeToInsert)
            else:
                self.setTail(nodeToInsert)
        
    
    def removeNodesWithValue(self, value):
        k = self.head
        while k != None:
            ntr = k
            k = k.next
            print("ntr: ", ntr.value)
            if ntr.value == value:
                self.remove(ntr)
                #print("{} removed. dll: {}".format(ntr.value, self.serialize()))
            

    # 2
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # 1
    def containsNodeWithValue(self, value):
        k = self.head
        while k is not None:
            if k.value == value:
                return True
            k = k.next
        return False

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return self

        k = self.head
        while k.next != None:
            k = k.next
        k.next = node
        node.prev = k
        self.tail = node # update tail
        return self

    # dir: True is forwards, False is backwards
    def serialize(self, dir=True):
        s = ""
        k = self.head
        if dir == False:
            k = self.tail

        while k != None:
            s += "{} ".format(k.value)
            
            if dir == True: 
                k = k.next
            else: 
                k = k.prev
        return s

class Test(unittest.TestCase):
    # BEGIN provided functions
    def expectEmpty(self, linkedList):
        self.assertEqual(linkedList.head, None)
        self.assertEqual(linkedList.tail, None)

    def expectHeadTail(self, linkedList, head, tail):
        self.assertEqual(linkedList.head, head)
        self.assertEqual(linkedList.tail, tail)

    def expectSingleNode(self, linkedList, node):
        self.assertEqual(linkedList.head, node)
        self.assertEqual(linkedList.tail, node)

    def getNodeValuesHeadToTail(self, linkedList):
        values = []
        node = linkedList.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def getNodeValuesTailToHead(self, linkedList):
        values = []
        node = linkedList.tail
        while node is not None:
            values.append(node.value)
            node = node.prev
        return values

    def removeNodes(self, linkedList, nodes):
        for node in nodes:
            linkedList.remove(node)
    # END provided functions

    def listFromPrompt(self):
        dll = DoublyLinkedList()
        dll.head = DLLNode(1)
        for i in range(2, 7):
            dll.append(DLLNode(i))
        s = dll.serialize(True)
        print("serialized list: ", s)
        return dll
    
    def test_containsNodeWithValue(self):
        dll = self.listFromPrompt()
        ans = dll.containsNodeWithValue(3)
        print("ans:", ans)

    def test_remove(self):
        n1 = DLLNode(1)
        n2 = DLLNode(2)
        n3 = DLLNode(3)
        n4 = DLLNode(4)
        dll = DoublyLinkedList()
        dll.append(n1).append(n2).append(n3).append(n4)
        print("dll before remove: ", dll.serialize())
        print("head obj: ", dll.head)
        print("head: {}, tail: {}".format(dll.head.value, dll.tail.value))
        print("n1 obj: {}, n1 val: {}, prev: {}".format(n1, n1.value, n1.prev))
        dll.remove(n1)
        print("after remove")
        print("eval: ", n1 == dll.head)
        print("dll after remove: ", dll.serialize())

    def test_removeNodesWithValue(self):
        dll = self.listFromPrompt()
        dll.append(DLLNode(4))
        print("test_removeNodesWithValue: dll: ", dll.serialize())
        dll.removeNodesWithValue(4)
        #dll.removeNodesWithValue(1)
        print("dll after removing nodes with value: ", dll.serialize())
        print(" head: {}, tail: {}".format(dll.head.value, dll.tail.value))

    def test_insertAtPosition(self):
        dll = DoublyLinkedList()
        dll.insertAtPosition(0, DLLNode(100))
        dll.insertAtPosition(0, DLLNode(200))
        print("dll after insert at position:", dll.serialize())

    def test_insertBefore(self):
        n1 = DLLNode(1); n2 = DLLNode(2); n3 = DLLNode(3); n4 = DLLNode(4)
        dll = DoublyLinkedList()
        dll.append(n1).append(n2).append(n3).append(n4)
        dll.insertBefore(n4, DLLNode(100))
        print("test_insertBefore: ", dll.serialize())
        
    def test_insertAfter(self):
        n1 = DLLNode(1); n2 = DLLNode(2); n3 = DLLNode(3); n4 = DLLNode(4)
        dll = DoublyLinkedList()
        dll.append(n1).append(n2).append(n3).append(n4)
        print("test_insertAfter: initial list: ", dll.serialize())
        dll.insertAfter(n4, DLLNode(100))
        print("test_insertAfter: ", dll.serialize())

    def test_setHead(self):
        dll = self.listFromPrompt()
        dll.setHead(DLLNode(100))
        print("test_setHead: ", dll.serialize())

    def test_setTail(self):
        dll = self.listFromPrompt()
        dll.setTail(DLLNode(100))
        print("test_setTail: ", dll.serialize())

    def test_case2(self):
        linkedList = DoublyLinkedList()
        first = DLLNode(1)
        second = DLLNode(2)
        nodes = [first, second]

        # linkedList.setHead(first)
        # linkedList.setTail(second)
        # print("A: ", linkedList.serialize())
        # self.expectHeadTail(linkedList, first, second)

        # self.removeNodes(linkedList, nodes)
        # self.expectEmpty(linkedList)
        # linkedList.setHead(first)
        # linkedList.insertAfter(first, second)
        # print("B: ", linkedList.serialize())
        # self.expectHeadTail(linkedList, first, second)

        # self.removeNodes(linkedList, nodes)
        # linkedList.setHead(first)
        # linkedList.insertBefore(first, second)
        # print("C: ", linkedList.serialize())
        # self.expectHeadTail(linkedList, second, first)

        self.removeNodes(linkedList, nodes)
        linkedList.insertAtPosition(1, first)
        linkedList.insertAtPosition(2, second)
        print("D: ", linkedList.serialize())
        self.expectHeadTail(linkedList, first, second)

        self.removeNodes(linkedList, nodes)
        linkedList.insertAtPosition(2, first)
        linkedList.insertAtPosition(1, second)
        print("E: ", linkedList.serialize())
        self.expectHeadTail(linkedList, second, first)


    def test_case4(self):
        linkedList = DoublyLinkedList()
        first = DLLNode(1)
        second = DLLNode(2)
        third = DLLNode(3)
        fourth = DLLNode(3)
        fifth = DLLNode(3)
        sixth = DLLNode(6)
        seventh = DLLNode(7)

        linkedList.setHead(first)
        linkedList.insertAfter(first, second)
        linkedList.insertAfter(second, third)
        linkedList.insertAfter(third, fourth)
        linkedList.insertAfter(fourth, fifth)
        linkedList.insertAfter(fifth, sixth)
        linkedList.insertAfter(sixth, seventh)
        self.assertEqual(self.getNodeValuesHeadToTail(linkedList), [1, 2, 3, 3, 3, 6, 7])
        self.assertEqual(self.getNodeValuesTailToHead(linkedList), [7, 6, 3, 3, 3, 2, 1])
        self.expectHeadTail(linkedList, first, seventh)
        linkedList.remove(second)
        self.assertEqual(self.getNodeValuesHeadToTail(linkedList), [1, 3, 3, 3, 6, 7])
        self.assertEqual(self.getNodeValuesTailToHead(linkedList), [7, 6, 3, 3, 3, 1])
        self.expectHeadTail(linkedList, first, seventh)
        linkedList.removeNodesWithValue(1)
        self.assertEqual(self.getNodeValuesHeadToTail(linkedList), [3, 3, 3, 6, 7])
        self.assertEqual(self.getNodeValuesTailToHead(linkedList), [7, 6, 3, 3, 3])
        self.expectHeadTail(linkedList, third, seventh)
        linkedList.removeNodesWithValue(3)
        self.assertEqual(self.getNodeValuesHeadToTail(linkedList), [6, 7])
        self.assertEqual(self.getNodeValuesTailToHead(linkedList), [7, 6])
        self.expectHeadTail(linkedList, sixth, seventh)
        linkedList.removeNodesWithValue(7)
        self.assertEqual(self.getNodeValuesHeadToTail(linkedList), [6])
        self.assertEqual(self.getNodeValuesTailToHead(linkedList), [6])
        self.expectHeadTail(linkedList, sixth, sixth)

def main():
    test = Test()
    #test.listFromPrompt()
    #test.test_containsNodeWithValue()
    #test.test_remove()
    test.test_removeNodesWithValue()
    #test.test_insertAtPosition()
    #test.test_insertBefore()
    #test.test_insertAfter()
    #test.test_setHead()
    #test.test_setTail()
    #test.test_case2()
    #test.test_case4()

if __name__ == "__main__":
    main()