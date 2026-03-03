'''
https://leetcode.com/problems/subtree-of-another-tree/
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        
        sameTreeFromNode = False
        if t and s.val == t.val:
            sameTreeFromNode = self.isSameTree(s, t)
            print("sameTreeFromNode for s:{}, t:{}: {}".format(s.val, t.val, sameTreeFromNode))
        
        if sameTreeFromNode == True:
            return sameTreeFromNode

        sLeft = self.isSubtree(s.left, t)
        sRight = self.isSubtree(s.right, t)
        return sLeft or sRight
    
    def isSameTree(self, s, t):
        if s == None or t == None:
            return True
        
        if (s.left and not t.left) or (s.right and not t.right): 
            return False
        
        if (t.left and not s.left) or (t.right and not s.right):
            return False

        if s.val != t.val:
            return False

        isSameTreeLeft = self.isSameTree(s.left, t.left)
        isSameTreeRight = self.isSameTree(s.right, t.right)
        return isSameTreeLeft and isSameTreeRight
    
    def test1(self): # expected true
        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        res = self.isSubtree(s,t)
        print("test1 res: ", res)

    def test2(self): # expected false
        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)
        s.left.right.left = TreeNode(0)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        res = self.isSubtree(s,t)
        print("test2 res: ", res)

    def test3(self): #expected false
        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)
        t.left.left = TreeNode(1)

        res = self.isSubtree(s,t)
        print("test3 res: ", res)

    def test4(self): #expected false
        s = TreeNode(1)
        t = TreeNode(0)
        res = self.isSubtree(s,t)
        print("test4 res: ", res)

s = Solution()
#s.test1()
#s.test2()
#s.test3()
s.test4()