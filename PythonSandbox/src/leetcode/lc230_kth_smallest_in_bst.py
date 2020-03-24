'''
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int: 
        #using inorder traversal, can get sorted array of values
        def helper(root, values):
            if root == None:
                return
            
            helper(root.left,values)
            values.append(root.val)
            helper(root.right,values)
            
        values=[]
        helper(root, values)
        return values[k-1]
    
    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        k=1
        res = self.kthSmallest(root, k)
        print("test1 res: ", res)
    
    def test2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right= TreeNode(4)
        root.left.left.left = TreeNode(1)
        k = 3
        res = self.kthSmallest(root, k)
        print("test2 res: ", res)

sol = Solution()
#sol.test1()
sol.test2()
