"""
Invert binary tree: for each node, swap left and right child nodes
"""
from utils.binary_tree_utils import BinaryTreeUtils as Utils

class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Prob:
    """ Complexity
    Time: O(n): all nodes must be traversed.
    Space: O(1): for each node there is just a temp node variable, but previous traversals are not stored.
    """
    @staticmethod
    def invertBinaryTree(tree):
        if tree == None:
            return tree
        print("node: ", tree.value)
        temp = tree.left
        if temp != None: print("    temp: ", temp.value)
        tree.left = tree.right
        if tree.left != None: print("    left: ", tree.left.value)
        tree.right = temp
        if tree.right != None: print("    right: ", tree.right.value)
        
        Prob.invertBinaryTree(tree.left)
        Prob.invertBinaryTree(tree.right)
        
    @staticmethod
    def tree1():
        tree = BTNode(1)
        tree.left = BTNode(2); tree.right = BTNode(3)
        tree.left.left=BTNode(4); tree.left.right=BTNode(5);tree.right.left=BTNode(6);tree.right.right=BTNode(7)
        tree.left.left.left=BTNode(8); tree.left.left.right=BTNode(9)
        return tree
    
    @staticmethod
    def test_invertBinaryTree():
        tree = Prob.tree1()
        Utils.printBT(tree)
        Prob.invertBinaryTree(tree)
        Utils.printBT(tree)
        
        
Prob.test_invertBinaryTree()