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

# Quickly build a list
class List:
    def __init__(self, nums):
        self.head, p1 = None, None
        self.length = 0
        for i,n in enumerate(nums):
            nInt = int(n)
            if self.head == None:
                self.head = ListNode(nInt)
                self.length += 1
                p1 = self.head
            else:
                p1.next = ListNode(nInt)
                self.length += 1
                p1 = p1.next

    def getHead(self):
        return self.head
    
    def getLength(self):
        return self.length
    
    def printList(self):
        p1 = self.head
        s = ""
        while p1 != None:
            s += (str(p1.val) + " -> ")
            p1 = p1.next
        s += "NULL"
        print(s)
            

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
        while n != None:
            print("val: ", n.val)
            n = n.next

    def llToArray(self, head):
        p = head
        result = []
        while p != None:
            result.append(p.val)
            p = p.next
        return result

    def getRevStr(self, ll):
        p1 = ll
        revStr = ""
        while p1 != None:
            revStr = str(p1.val) + revStr
            p1 = p1.next
        return revStr

    """ Using helper function and auxiliary class 
    Runtime: Beats 85.51%, Memory: Beats 83.33%
    """
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = self.getRevStr(l1)
        s2 = self.getRevStr(l2)
        s1s2Sum = int(s1) + int(s2)
        sumStr = str(s1s2Sum)
        sumStrListRev = list(sumStr)[::-1]
        resultLL = List(sumStrListRev)
        return resultLL.getHead()


    def testList(self):
        a = [i for i in range(10, 51, 10)]
        # print("a:", a)
        l1 = List(a)
        l1.printList()
        length = l1.getLength()
        print("length: ", length)
        h = l1.getHead().val
        print("head val: ", h)

    def test2(self):
        l1 = List([2,4,3])
        l1.printList()
        l2 = List([5,6,4])
        l2.printList()
        res = self.addTwoNumbers_2(l1.getHead(), l2.getHead())
        resArr = self.llToArray(res)
        print("resArr: ", resArr)

    """ Using carry number
    """
    def addTwoNumbers_3(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        p1 = l1
        p2 = l2

        l3Head = None
        p3 = None

        while p1 != None or p2 != None:
            p1p2Sum = 0
            if p1 != None and p2 != None:
                p1p2Sum = p1.val + p2.val
                p1 = p1.next
                p2 = p2.next
            elif p1 == None and p2 != None:
                p1p2Sum = p2.val
                p2 = p2.next
            else:
                p1p2Sum = p1.val
                p1 = p1.next

            p1p2Sum += carry
            placedValue = 0
            if p1p2Sum >= 10:
                carry = 1
                placedValue = p1p2Sum % 10
            else:
                carry = 0
                placedValue = p1p2Sum
                
            if l3Head == None:
                l3Head = ListNode(placedValue)
                p3 = l3Head
            else:
                p3.next = ListNode(placedValue)
                p3 = p3.next

        # final check for carry over
        if carry >= 1:
            p3.next = ListNode(carry)

        return l3Head


    def test3(self):
        l1 = List([9,9,9,9,9,9,9])
        l1.printList()
        l2 = List([9,9,9,9])
        l2.printList()
        res = self.addTwoNumbers_3(l1.getHead(), l2.getHead())
        resArray = self.llToArray(res)
        print("resArray: ", resArray)    


sol = Solution()
# sol.test1()
# sol.test2()
# sol.testList()
sol.test3()
