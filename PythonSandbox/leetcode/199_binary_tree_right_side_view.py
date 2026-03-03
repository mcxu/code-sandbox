'''
https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        depthMap = {}
        depth = 0
        self.helper(root, depth, depthMap)

        out = []
        for key in sorted(depthMap.keys()):
            lastElt = depthMap[key]
            out.append(lastElt)
        return out
    
    def helper(self, root, depth, depthMap):
        if root == None:
            return
        
        depthMap[depth] = root.val
        
        self.helper(root.left, depth+1, depthMap)
        self.helper(root.right, depth+1, depthMap)
    
    def test1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        res = self.rightSideView(root)
        print("test1 res: ", res)

    def test2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)

        res = self.rightSideView(root)
        print("test2 res: ", res)

    def test3(self):
        root = TreeNode(1)
        n = root
        for i in range(2, 11):
            n.left = TreeNode(i)
            n = n.left

        res = self.rightSideView(root)
        print("test3 res: ", res)

s = Solution()
#s.test1()
#s.test2()
s.test3()