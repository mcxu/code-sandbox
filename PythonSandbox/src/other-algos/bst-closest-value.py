"""
Find the closest value to a target in a Binary Search Tree
"""

import math
from unittest import TestCase

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None: self.left = BST(value)
            else: self.left.insert(value)
        else:
            if self.right is None: self.right = BST(value)
            else: self.right.insert(value)
        return self

class BSTClosestValue:
    def findClosestValueInBst(self, tree, target):
        print("\n===================== target: {}".format(target))
        closest = self.helper(tree, target, math.inf)
        print("closest was: {}".format(closest))
        return closest
        
    def helper(self, tree, target, closest):
        if(tree is None):
            return closest
        print("=== tree value: {}, target: {}, closest:{}".format(tree.value, target, closest))
        tvd = self.diff(target, tree.value)
        print("tvd:{}".format(tvd))
        if(tvd < self.diff(target,closest)):
            closest = tree.value
            print("closest is now: {}".format(closest))
        
        if(target < tree.value):
            print("left node")
            return self.helper(tree.left, target, closest)	
        elif(target > tree.value):
            print("right node")
            return self.helper(tree.right, target, closest)
        else:
            return closest
        
    def diff(self,v1,v2):
        return abs(v2-v1)

class TestClass(TestCase):
    def test1(self, bcvClass):
        exampleBST = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
        .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
        .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
        .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)

        self.assertEqual(bcvClass.findClosestValueInBst(exampleBST,902), 1001, msg="902~1001")

def main():
    bcv = BSTClosestValue()
    tc = TestClass()
    tc.test1(bcv)

main()