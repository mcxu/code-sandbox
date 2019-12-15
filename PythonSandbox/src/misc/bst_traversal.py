"""
{In,Pre,Post}order traversal of Binary Search Tree.

Complexities
Time: O(n): traverse through all nodes.
Space: O(n): because there is a recursive call for each node.
"""
from misc.bst_construction import BST
from utils.binary_tree_utils import BinaryTreeUtils as Utils

def inOrderTraverse(tree, array):
    if tree == None:
        return array
    
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree == None:
        return array
    
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree == None:
        return array
    
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array


def tree1():
    test1 = BST(10).insert(5).insert(15)
    #Utils.printBT(test1)
    return test1

def testCase1():
    array = inOrderTraverse(tree1(), [])
    print("inOrderTraverse: ", array)
    array = preOrderTraverse(tree1(), [])
    print("preOrderTraverse: ", array)
    array = postOrderTraverse(tree1(), [])
    print("postOrderTraverse: ", array)

#tree1()
testCase1()