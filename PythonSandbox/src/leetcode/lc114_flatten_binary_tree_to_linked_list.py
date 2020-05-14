'''
114. Flatten Binary Tree to Linked List
*flatten in-place without returning the root
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.value = self.val
        self.left = None
        self.right = None

class Solution:
    '''
    Let n = num nodes in tree.
    Time complexity: O(n), because the algorithm recurses over n nodes.
    Space complexity: O(1), because there is a constant number of additional pointers needed (tmpRight, and tmpLeft).
    '''
    def flatten(self, root):
        if root == None:
            return None
        
        if root.left != None:
            tmpRight = root.right
            root.right = root.left
            root.left = None
            
            tmpLeft = root.right
            while tmpLeft.right != None:
                tmpLeft = tmpLeft.right
            
            tmpLeft.right = tmpRight
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        return None

    def tree1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        return root
    
    def tree2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)
        return root

    def tree3(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        return root
    
    def test1(self):
        root = self.tree1()
        self.flatten(root) #root flattened
        print("root: ", root.val)
        print("root.right: ", root.right.val)


    def test2(self):
        root = self.tree2()
        self.flatten(root)
        rf = root
        print("rf root: ", rf.val)
        print("rf.left: ", rf.left)
        print("rf.right: ", rf.right.val)
        print("rf.right.left: ", rf.right.left)
        print("rf.right.right: ", rf.right.right.val)
    
sol = Solution()
sol.test1()
#sol.test2()

        