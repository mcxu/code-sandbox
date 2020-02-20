'''
113. Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        path = []
        validPaths = []
        self.helper(root, sum, 0, path, validPaths)
        return validPaths
    
    def helper(self, root, sum, runSum, path, validPaths):
        print("---")
        if root == None:
            print("root is none, return nothing")
            return
        runSum += root.val
        path.append(root.val)
        print("root: {}, runSum: {}, path: {}".format(root.val, runSum, path))
        
        if root.left is None and root.right is None and runSum == sum:
            validPaths.append(path.copy())
            print("validPaths: ", validPaths)
        
        print("A")
        self.helper(root.left, sum, runSum, path, validPaths)
        print("end A")
        print("B")
        self.helper(root.right, sum, runSum, path, validPaths)
        print("end B")
        
        print("POPPING, root: ", root.val)
        path.pop()
        print("AFTER POP: path: ", path)
    
    def test1(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        
        paths = self.pathSum(root, 22)
        print("test1: paths: ", paths)

sol = Solution()
sol.test1()