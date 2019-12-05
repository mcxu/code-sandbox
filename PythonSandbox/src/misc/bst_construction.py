"""
BST Construction
"""
import unittest
from utils.binary_tree_utils import BinaryTreeUtils as Utils

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        
        return self

    def contains(self, value):
        if self.value == value:
            return True
        
        if value < self.value:
            if self.left == None:
                return False
            return self.left.contains(value)
        else:
            if self.right == None:
                return False
            return self.right.contains(value)
    
    """
    TODO: remove function not working yet
    Involves getting the leftmost value of the right subtree.
    """
    def remove(self, value, parentNode = None):
        if self == None:
            return
        print("value: {}, self.value: {}".format(value, self.value))
        
        if value == self.value:
            print("match1: value: {}, self.value: {}".format(value, self.value))
            self.left = None
            self.right = None
            self = None
            return
        
        if value < self.value:
            if self.left != None:
                self.left.remove(value)
        else:
            if self.right != None:
                self.right.remove(value)
        
        
class Test(unittest.TestCase):
    
    def testInsert1(self):
        tree = BST(10).insert(1).insert(11)
        Utils.printBT(tree)
    
    def testContains1(self):
        tree = BST(10).insert(1).insert(11)
        Utils.printBT(tree)
        r = tree.contains(9)
        print("r: ", r)
        
        tree2 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
        Utils.printBT(tree2)
        r2 = tree2.contains(2)
        print("r2: ", r2)
    
    def testRemove1(self):
        tree2 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
        Utils.printBT(tree2)
        r2 = tree2.contains(15)
        print("r2: ", r2)
        print("---")
        tree2.remove(15)
        Utils.printBT(tree2)
        r3 = tree2.contains(15)
        print("r3: ", r3)
    
    def testCase1(self):
        test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
        Utils.printBT(test1)
        

def main():
    t = Test()
    #t.testInsert1()
    #t.testCase1()
    #t.testContains1()
    t.testRemove1()

main()