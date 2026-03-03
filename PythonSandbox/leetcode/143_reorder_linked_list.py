'''
143. Reorder List
https://leetcode.com/problems/reorder-list/description/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Time complexity: O(n), n ~ length of linked list
    Space complexity: O(n), since the array to keep track of index was used.
    '''
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # add all nodes into an array
        arr = []
        n = head
        while n != None:
            arr.append(n)
            n = n.next
        
        exclusiveLim = None
        if len(arr) % 2 == 0: # even num of nodes
            exclusiveLim = len(arr) // 2
        else:
            exclusiveLim = (len(arr) // 2) + 1

        for i in range(exclusiveLim):
            a = arr[i]
            b = arr[len(arr) - 1 - i]
            
            if i == exclusiveLim - 1 and (a == b or a.next == b):
                b.next = None
                break

            b.next = a.next
            a.next = b

        return head
            
    
    def createLinkedList(self, arr):
        if not arr:
            return None
        
        head = ListNode(arr[0])
        n = head
        for i in range(1, len(arr)):
            n.next = ListNode(arr[i])
            n = n.next
        return head

    def linkedListToArray(self, head):
        arr = []
        n = head
        while n != None:
            arr.append(n.val)
            n = n.next
        return arr

    def test(self):
        cases = [
            # dict(head = [1,2,3,4], expected = [1,4,2,3]),
            dict(head = [1,2,3,4,5], expected = [1,5,2,4,3]),
            # dict(head = [1,2,3], expected = [1,3,2]),
            # dict(head = [1,2], expected = [1,2])
        ]

        for case in cases:
            caseArr = case["head"]
            caseExp = case["expected"]

            headFromCase = self.createLinkedList(caseArr)
            # caseArrFromLL = self.linkedListToArray(caseLL)
            # print("caseArrFromLL: ", caseArrFromLL)

            headFromFunc = self.reorderList(headFromCase)

            result = self.linkedListToArray(headFromFunc)
            print("result: ", result)
            assert result == caseExp

sol = Solution()
sol.test()


'''
        for i in range(len(arr)//2):
            print(f"======= i= {i} =======")

            # initalize pointers
            print("initialize pointers")
            a = arr[i]
            b = a.next
            c = arr[len(arr)-2-i]
            d = c.next

            # reorder outer pointers
            print("reorder outer pointers")
            a.next = d
            print("a.next: ", a.next.val)
            d.next = b
            print("d.next: ", d.next.val)

            # account for the case where the beginning and ending pointers already intersect
            if i == 0: 
                if a==c and b==d: # there must be only 2 values if logic falls into this at i = 0
                    print("i ==0 and elif")
                    a.next = None
                    d.next = a
                    head = d
                elif b == c: # there must be only 3 values if the logic falls into this at i = 0
                    print("i ==0 and b==c")
                    b.next = None
                break

            # increment beginning pointers
            print("increment beginning pointers")
            a = b
            print("a= ", a.val)
            b = b.next
            print("b= ", b.val)

            # reorder inner pointers
            a.next = c
            c.next = b
            
            # breakout condition
            if b == c:
                c.next = None
                break
            elif b.next == c:
                c.next = b
                b.next = None
                break
            
            # decrement ending pointers
            c = arr[len(arr)-2-i-1]
            d = c.next
        
        return head
'''