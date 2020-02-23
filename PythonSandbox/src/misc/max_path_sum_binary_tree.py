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
https://www.youtube.com/watch?v=peyO-Nu1jGc
'''

class BTNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Prob:
    '''
    Time complexity: O(n), n=number of nodes, since traversal covers all n nodes.
    Space complexity: O(log(n)), or that it's proportional to the depth of the tree.
        If we have a relatively balanced tree, then O(log(n)) is an average.
        If we have a very unbalanced tree (worst case), like a linked list, 
        then space complexity is O(n), since there will be n calls on the recursive call stack.
    '''
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
            
            mpsUpToLeftChild = currPathSum(tree.left)
            mpsUpToRightChild = currPathSum(tree.right)
            
            # This is picking a singular path from 3 choices: (1) new path starting from tree.value if adding 
            # mpsUpToLeftChild or mpsUpToRightChild actually results in decreasing the tree.value.
            # (2) Path from left child to value. (3) Path from right child to value.
            mpsUpToCurrNode = max(tree.value, tree.value+mpsUpToLeftChild, tree.value+mpsUpToRightChild)
            
            # This is determining where the uppermost node is in the path, since at this node, 
            # the root value must be added to the left and right MPS. So if this is greater than 
            # The mpsUpToCurrNode (for a singular path), then it must be the new "triangle".
            mpsTriangle = max(mpsUpToCurrNode, mpsUpToLeftChild + tree.value + mpsUpToRightChild)
            
            # If the new triangle is greater than the current mps, then update
            mps = max(mps, mpsTriangle)
            
            # Return mpsUpToCurrNode because the recursive calls require the greatest PATH sum,
            # whether its left->root, or right->root. (child->root since this is postorder traversal.)
            # It's not asking for the triangle, but the PATH.
            return mpsUpToCurrNode
         
        currPathSum(tree)
        return mps


    @staticmethod
    def maxPathSum2(tree):
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
        tree = BTNode(1) # correct ans: 18
        #tree = BTNode(-1) # correct ans: 16
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

#Prob.test1()
#Prob.test2() 
#Prob.test3()
Prob.test4()

