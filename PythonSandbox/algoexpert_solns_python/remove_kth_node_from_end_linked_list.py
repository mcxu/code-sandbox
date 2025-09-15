'''
Remove kth node from end of linked list
Sample input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, 4
Sample output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 (value 6 has been removed)
'''
from platform import node

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Prob:
    @staticmethod
    def removeKthNodeFromEnd(head, k):
        if k < 1:
            return head
        
        tmp = head
        maxIndex = 0
        print("k: ", k)
        # keep track of index
        while tmp.next != None:
            maxIndex += 1
            tmp = tmp.next
        print("maxIndex: ", maxIndex) 
        
        targetIndex = maxIndex - k
        print("targetIndex: ", targetIndex)
        
        if targetIndex <= -1:
            head = head.next
        else:
            tmp = head
            i = 0
            while tmp != None:
                if i == targetIndex:
                    print("targetValue: ", tmp.value)
                    tmp.next = tmp.next.next
                    return head
                i += 1
                tmp = tmp.next
        return head
        
    @staticmethod
    def list1():
        nodes = []
        for v in range(0,10):
            nodes.append(LinkedList(v))
        
        for i in range(0, len(nodes)-1):
            node = nodes[i]
            node.next = nodes[i+1]
        
        head = nodes[0]
        #Prob.printList(head)
        return head

    @staticmethod
    def list2():
        nodes = []
        for v in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            nodes.append(LinkedList(v))
        
        for i in range(0, len(nodes)-1):
            node = nodes[i]
            node.next = nodes[i+1]
        
        head = nodes[0]
        return head
    
    @staticmethod
    def printList(node):
        print("printList: ", end="")
        l = []
        head = node
        while head != None:
            l.append(head.value)
            head = head.next
        print(l, end="\n")
        return l
        
    @staticmethod
    def test1():
        head = Prob.list1()
        k = 20
        result = Prob.removeKthNodeFromEnd(head, k)
        print("test1 result:")
        Prob.printList(result)
    
    @staticmethod
    def test2():
        head = Prob.list2()
        Prob.printList(head)
        k = 10
        result = Prob.removeKthNodeFromEnd(head, k)
        print("test2 result:")
        res = Prob.printList(result)
        
#Prob.list1()
#Prob.test1()
#Prob.list2()
Prob.test2()

