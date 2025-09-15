class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root.left and root.right and (root.left.val != root.right.val):
            return False
        
        return self.dfs(root.left, root.right)
    

    def dfs(self, leftNode, rightNode):

        if leftNode == None and rightNode == None:
            return True

        if leftNode and not rightNode:
            return False
        
        if not leftNode and rightNode:
            return False

        if leftNode.left and rightNode.right and leftNode.left.val != rightNode.right.val:
            return False

        if leftNode.right and rightNode.left and leftNode.right.val != rightNode.left.val:
            return False
            
        leftIsSym = self.dfs(leftNode.left, rightNode.right)
        rightIsSym = self.dfs(leftNode.right, rightNode.left)

        return leftIsSym and rightIsSym