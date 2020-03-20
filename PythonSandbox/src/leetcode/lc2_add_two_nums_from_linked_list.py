'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        tot1 = 0
        tot2 = 0
        p1 = 1
        p2 = 1
        
        while n1 != None or n2 != None:
            if n1 != None:
                tot1 += n1.val * p1
                p1 *= 10
                n1 = n1.next
            if n2 != None:
                tot2 += n2.val * p2
                p2 *= 10
                n2 = n2.next     
            
        print("tot1: {}, tot2: {}".format(tot1, tot2))
        totBothStr = str(tot1 + tot2)
        
        # start building the sum in LL form.
        currPointer = ListNode(int(totBothStr[0]))
        for i in range(1, len(totBothStr)):
            prevPointer = ListNode(int(totBothStr[i]))
            prevPointer.next = currPointer
            currPointer = prevPointer
        
        return currPointer
    
    def test1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        n = self.addTwoNumbers(l1, l2)
        print("test1 list: ")
        while n != None:
            print("val: ", n.val)
            n = n.next

sol = Solution()
sol.test1()
