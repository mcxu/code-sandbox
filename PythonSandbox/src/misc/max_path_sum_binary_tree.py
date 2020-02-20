'''
Max Path Sum in Binary Tree

Given binary tree, return the max path sum.

Sample input:
        1
   2        3
4    5    6   7

Sample output: 18 (sum(1,2,5,3,7))
'''

class BTNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Prob:
    @staticmethod
    def maxPathSum(tree):
        if tree == None:
            return 0
        return Prob.helper(tree, 0)

    @staticmethod
    def helper(tree, s):
        if tree == None:
            return s
        print("curr tree.value: {}, sum: {}".format(tree.value,s))
        
#         if tree.left and not tree.right:
#             print("A")
#             s += tree.left.value
#         elif not tree.left and tree.right:
#             print("B")
#             s += tree.right.value
#         elif tree.left and tree.right:
#             print("C")
#             s += max(tree.left.value, tree.right.value)
#         else:
#             print("D")
#             s += tree.value
#         print("sum is: ", s)
         
        sumWithL = Prob.helper(tree.left, s+tree.value)
        #print("sumWithL: ", sumWithL)
        sumWithR = Prob.helper(tree.right, s+tree.value)
        #print("sumWitR: ", sumWithR)
        
        print("E")
        return max(sumWithL, sumWithR)


    @staticmethod
    def test1():
        tree = BTNode(1)
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

Prob.test1()
#Prob.test2() 
       