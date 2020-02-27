'''
Floyd's Cycle Detection Algorithm (Tortoise and Hare Algorithm)

Version 1: Given linked list, return true if cycle exists, false otherwise.
Version 2: Given linked list, if cycle exists, break the cycle, then 
    return the node value where the cycle begins. If the LL doesn't have a cycle, 
    then return None
    
Walkthrough: https://www.youtube.com/watch?v=zbozWoMgKW0
Theory: https://www.youtube.com/watch?v=LUm2ABqAs1w

'''
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def append(self, value):
        self.next = Node(value)
        return self.next

class Prob:
    @staticmethod
    def hasCycleV1(head):
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            print("fast value: ", fast.value)
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
    @staticmethod
    def hasCycleV2(head):
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycleStartVal = Prob.breakCycle(head, slow)
                return cycleStartVal
        
        return None
    
    @staticmethod
    def breakCycle(head, slow):
        n = head
        while n.next != slow.next:
            n = n.next
            slow = slow.next
        
        cycleStartVal = slow.next.value
        slow.next = None
        return cycleStartVal
        

    @staticmethod
    def list1():
        head = Node(0)
        beforeCycle = head.append(1).append(2)
        startCycle = beforeCycle.append(3).append(4).append(5)
        startCycle.next = beforeCycle
        return head
    
    @staticmethod
    def list2():
        head = Node(0)
        beforeCycle = head.append(1).append(2).append(3).append(4)
        startCycle = beforeCycle.append(5).append(6).append(7).append(8)
        startCycle.next = beforeCycle
        return head
    
    @staticmethod
    def list3():
        head = Node(0)
        beforeCycle = head.append(1).append(2).append(3).append(4)
        startCycle = beforeCycle.append(5).append(6).append(7).append(8).append(9)
        startCycle.next = beforeCycle
        return head
    
    @staticmethod
    def list4():
        head = Node(0)
        beforeCycle = head.append(1).append(2).append(3)
        startCycle = beforeCycle.append(5).append(6)
        startCycle.next = beforeCycle
        return head
    
    @staticmethod
    def list5():
        head = Node(0)
        head.append(1).append(2).append(3).append(4).append(5).append(6).append(7).append(8)
        return head
    
    @staticmethod
    def printLL(head):
        n = head
        while n != None:
            print("n=", n.value)
            n = n.next
            time.sleep(1)
    
    @staticmethod
    def test1():
        #head = Prob.list1()
        #head = Prob.list4()
        head = Prob.list5()
        ans = Prob.hasCycleV1(head)
        print("test1: ans: ", ans)
    
    @staticmethod
    def test2():
        #head = Prob.list1()
        #head = Prob.list2()
        #head = Prob.list3()
        head = Prob.list4()
        #head = Prob.list5()
        ans = Prob.hasCycleV2(head)
        print("test2: ans: ", ans)
        
Prob.test1()
#Prob.test2()

