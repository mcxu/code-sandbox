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
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass
    
    def removeNodesWithValue(self, value):
        k = self.head
        while k != None:
            if k.value == value:
                self.remove(k)
            k = k.next

    # 2
    def remove(self, node):
        if node == self.head:
            node.next.prev = node.prev
            node = node.next
            self.head = node
        elif node == self.tail:
            node.prev.next = node.next
            node = node.prev
            self.tail = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    # 1
    def containsNodeWithValue(self, value):
        k = self.head
        while k is not None:
            if k.value == value:
                return True
            k = k.next
        return False

    # just used for testing
    def append(self, node):
        if self.head == None:
            self.head = node
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

class Test:
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
        dll.removeNodesWithValue(4)
        dll.removeNodesWithValue(1)
        print("dll after removing nodes with value: ", dll.serialize())
        print(" head: {}, tail: {}".format(dll.head.value, dll.tail.value))

def main():
    test = Test()
    #test.listFromPrompt()
    #test.test_containsNodeWithValue()
    #test.test_remove()
    test.test_removeNodesWithValue()

if __name__ == "__main__":
    main()