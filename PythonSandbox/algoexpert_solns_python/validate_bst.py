"""
Determine if a Binary Tree fits the criteria to be a Binary Search Tree.

Sample input:
        10
    5        15
  2   5   13    22
1          14
Sample output: True
"""
from misc.bst_construction import BST
from utils.binary_tree_utils import BinaryTreeUtils as Utils

class BTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class Prob:
    """
    Complexity
    Time: O(n) worst case, need to traverse all nodes for True case
    Space: O(d) where d is the depth of the tree
    """
    @staticmethod
    def validateBst(tree):
        maxVal = float("inf")
        minVal = -maxVal
        return Prob.helper(tree, minVal, maxVal)
        
    @staticmethod
    def helper(tree, minVal, maxVal):
        if tree == None:
            return True
        
        if tree.value < minVal or tree.value >= maxVal:
            return False
        
        # check if left subtree is valid: set maxVal to value of current node
        lv = Prob.helper(tree.left, minVal, tree.value)
        
        # check if right subtree is valid: set minVal to value of current node
        rv = Prob.helper(tree.right, tree.value, maxVal)
        
        return (lv & rv)
        
    @staticmethod
    def tree1():
        tree = BTNode(10)
        tree.left = BTNode(5)
        tree.right = BTNode(15)
        tree.left.left = BTNode(2)
        tree.left.right = BTNode(5)
        tree.left.left.left = BTNode(1)
        tree.right.left = BTNode(13)
        tree.right.right = BTNode(22)
        tree.right.left.right = BTNode(14)
        return tree
    
    @staticmethod
    def tree2():
        tree = (
            BST(10)
            .insert(5)
            .insert(15)
            .insert(5)
            .insert(2)
            .insert(1)
            .insert(22)
            .insert(-5)
            .insert(-15)
            .insert(-5)
            .insert(-2)
            .insert(-1)
            .insert(-22)
        )
        return tree
    
    @staticmethod
    def tree6():
        test6 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
        print("test6.left.right: ", test6.left.right.value)
        test6.left.right.right = BST(11)
        Utils.printBT(test6)
        return test6
    
    @staticmethod
    def test_validateBst():
        ans = Prob.validateBst(Prob.tree1())
        print("ans: ", ans)
    
    @staticmethod
    def test_validateBst2():
        ans = Prob.validateBst(Prob.tree2())
        print("ans: ", ans)
    
    @staticmethod
    def test_validateBst6():
        ans = Prob.validateBst(Prob.tree6())
        print("ans: ", ans)
    
#Prob.test_validateBst()
#Prob.tree2()
#Prob.test_validateBst2()
#Prob.tree6()
Prob.test_validateBst6()
