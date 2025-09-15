'''
https://leetcode.com/problems/insert-into-a-binary-search-tree/
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            root = TreeNode(val)
            return root
        
        self.helper(root,val)
        return root
        
    def helper(self, root, val):
        if root == None:
            return
        
        if not root.left and root.val > val:
            root.left = TreeNode(val)
            return
        if not root.right and root.val < val:
            root.right = TreeNode(val)
            return 
        
        if root.val < val:
            self.helper(root.right, val)
        elif root.val > val:
            self.helper(root.left, val)