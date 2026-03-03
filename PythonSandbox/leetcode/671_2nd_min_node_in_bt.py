'''
671. Second Minimum Node In a Binary Tree
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. 
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
More formally, the property root.val = min(root.left.val, root.right.val) always holds.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        def helper(root, values):
            if root == None:
                return
            
            values.add(root.val)
            helper(root.left, values)
            helper(root.right, values)
        
        values = set()
        helper(root, values)
        print("values: ", values)
        
        if not values:
            return -1
         
        if len(values) == 1:
            return -1
        
        # find 2nd min value
        for _ in range(2):
            minVal = float('inf')
            for val in values:
                if val < minVal:
                    minVal = val
                    print("minVal found: ", minVal)
            print("values: ", values)
            values.remove(minVal)
        print("minVal: ", minVal)
        return minVal
        
        
        
    def test1(self):
        root=TreeNode(2)
        root.left=TreeNode(2)
        root.right=TreeNode(5)
        root.right.left=TreeNode(5)
        root.right.right=TreeNode(7)
        self.findSecondMinimumValue(root)

sol = Solution()
sol.test1()

        