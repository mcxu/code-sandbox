'''
Max Path Sum in Binary Tree

Given binary tree, return the max path sum.

Sample input:
        1
   2        3
4    5    6   7

Sample output: 18 (sum(5,2,1,3,7))

https://leetcode.com/problems/binary-tree-maximum-path-sum/
https://www.youtube.com/watch?v=mOdetMWwtoI&t=725s
'''

class BTNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Prob:
    @staticmethod
    def maxPathSum(tree):
        # The var for storing the max path sum. This begins with -inf to ensure the algorithm works
        # for trees with only negative numbers.
        mps = -float('inf')
         
        def currPathSum(tree):
            nonlocal mps
            
            # If no node, then the max path sum to that node is 0
            if tree == None:
                return 0
            print("tree value: ", tree.value) 
            print("    mps: ", mps)
            
            # Do postorder traversal; access the root AFTER recursively calling left and right.
            # This is so that for each node, you have the previously computed mps for left and right
            # children, and work your way up. The comparison with 0 is so that if the current
            # node's tree.value is negative, it should not be included in the path.
            mpsUpToLeftChild = max(0, currPathSum(tree.left))
            mpsUpToRightChild = max(0, currPathSum(tree.right))
            
            # If the current sums up to each child + the node value is greater than previous mps,
            # then the current mps becomes that. Otherwise, say in the case where tree.value is negative,
            # the old mps is still the greatest.
            mps = max(mps, mpsUpToLeftChild + tree.value + mpsUpToRightChild)
            print("    mps updated: {} for tree value: {}".format(mps,tree.value))
            
            # Determine which path up to child + tree.value should be chosen
            mpsUpToCurrNode = max(mpsUpToLeftChild, mpsUpToRightChild) + tree.value
            print("    mpsUpToCurrNode: {} for tree value: {}".format(mpsUpToCurrNode, tree.value))
            
            return mpsUpToCurrNode
         
        currPathSum(tree)
        return mps

    @staticmethod
    def test1():
        #tree = BTNode(1) # correct ans: 18
        tree = BTNode(-1) # correct ans: 16
        tree.left = BTNode(2)
        tree.left.left = BTNode(4)
        tree.left.right = BTNode(5)
        tree.right = BTNode(3)
        tree.right.left = BTNode(6)
        tree.right.right = BTNode(7)
        
        s = Prob.maxPathSum(tree)
        print("test1: s: ", s)
    
    @staticmethod
    def test2():
        # correct ans: 6
        tree = BTNode(1)
        tree.left = BTNode(2)
        tree.right = BTNode(3)
        s = Prob.maxPathSum(tree)
        print("test2: s: ", s)
    
    @staticmethod
    def test3():
        tree = BTNode(-3)
        #tree = BTNode(3)
        s = Prob.maxPathSum(tree)
        print("test3: s: ", s)
    
    @staticmethod
    def test4():
        tree = BTNode(-2)
        tree.left = BTNode(-1)
        s = Prob.maxPathSum(tree)
        print("test4: s: ", s)

Prob.test1()
#Prob.test2() 
#Prob.test3()
#Prob.test4()

