"""
BST Construction

References:
https://www.journaldev.com/23086/binary-search-tree-bst-search-insert-remove
"""
import unittest
from utils.binary_tree_utils import BinaryTreeUtils as Utils

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self == None:
            return self
        
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
            print("contains value: ", self)
            return True
        
        if value < self.value:
            if self.left == None:
                return False
            return self.left.contains(value)
        else:
            if self.right == None:
                return False
            return self.right.contains(value)
        
        return False
    
    """
    Involves getting the leftmost value of the right subtree.
    """
    def remove(self, value, parentNode=None):
        if self == None:
            return self
            
        print("remove value: {}, self.value: {}, self addr: {}".format(value, self.value, self))
        if value < self.value:
            if self.left != None:
                self.left.remove(value, self)
        else:
            if self.right != None:
                self.right.remove(value, self)
        
        if value == self.value:
            if parentNode != None:
                print("target value found: {}, self.value: {}".format(value, self))
                print("parentnode: {}, parentNode value: {}".format(parentNode, parentNode.value))
                if self.right != None and self.left != None:
                    print("A: right and left both exist")
                    # successor is min value from the right branch
                    successor = self.right.findMinValNode() 
                    print("successor found: ", successor.value)
                    print("successor addr: ", successor)
                    svtemp = successor.value
                    self.remove(successor.value, parentNode) # remove successor node recursively
                    self.value = svtemp # replace current node value with minimum value
                elif self.right == None and self.left != None:
                    print("B: right is none, left exists")
                    self.value = self.left.value
                    self.left = None
                elif self.right != None and self.left == None:
                    print("C: right exists, left is none")
                    self.value = self.right.value
                    self.right = None
                else:
                    print("D: both are none")
                    if self == parentNode.right:
                        parentNode.right = None
                    elif self == parentNode.left:
                        parentNode.left = None
            else:
                # if parentNode is none, meaning that the top root is the target
                print("E")
                if self.right != None:
                    print("F")
                    successor = self.right.findMinValNode()
                    print("successor: {}, successor value: {}".format(successor, successor.value))
                    self.value = successor.value
                    # delete the successor node, which can be done recursively
                    self.right.remove(successor.value)
                else:
                    print("G")
                    print("self.value: {}".format(self.value))
                    self.value = self.left.value
                    print("self.value after reassign: ", self.value)
                    temp = self.left
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    
        return self    
    
    # find minimum value from root (self that calls this function)
    def findMinValNode(self):
        node = self # successor is min value from the right branch
        minVal = self.value
        minValNode = node
        while(node != None):
            if node.value < minVal:
                minVal = node.value
                minValNode = node
            node = node.left
        return minValNode
            
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
        ntr = 10
        print("before remove")
        r2 = tree2.contains(ntr)
        print("tree contains {}: {}".format(ntr, r2))
        tree2.remove(ntr)
        print("after remove")
        Utils.printBT(tree2)
        r3 = tree2.contains(ntr)
        print("tree contains {}: {}".format(ntr, r3))
    
    def testRemove2(self):
        tree = BST(15).insert(14).insert(22).insert(21)
        print("before remove")
        Utils.printBT(tree)
        ntr = 15
        print("removing ", ntr)
        tree.remove(ntr)
        print("after remove")
        Utils.printBT(tree)
    
    def testRemove3(self):
        tree = BST(15).insert(14).insert(22).insert(21).insert(24).insert(2).insert(100).insert(18)
        print("before remove")
        Utils.printBT(tree)
        ntr = 15
        print("removing ", ntr)
        tree.remove(ntr)
        print("after remove")
        Utils.printBT(tree)
    
    def testTree1(self):
        test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
        Utils.printBT(test1)
    
    def testTree2(self):
        tree = BST(10).insert(5).insert(7).insert(2).remove(10)
        Utils.printBT(tree)
#         tree.remove(10)
#         Utils.printBT(tree)

    def testTree4(self):
        tree = (BST(10)
            .insert(5)
            .insert(15)
            .insert(22)
            .insert(17)
            .insert(34)
            .insert(7)
            .insert(2)
            .insert(5)
            .insert(1)
            .insert(35)
            .insert(27)
            .insert(16)
            .insert(30)
            .remove(22)
            .remove(17)
            )
        Utils.printBT(tree)
#         tree.remove(22)
#         Utils.printBT(tree)
#         tree.remove(17).remove(22)
#         Utils.printBT(tree)

def main():
    t = Test()
    #t.testInsert1()
    #t.testTree1()
    #t.testContains1()
    #t.testRemove1()
    #t.testRemove2()
    #t.testRemove3()
    #t.testTree2()
    t.testTree4()

main()