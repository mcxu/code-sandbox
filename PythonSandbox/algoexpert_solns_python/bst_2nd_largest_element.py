'''
2nd largest element from a binary search tree
https://hackernoon.com/technical-interviewing-for-people-who-suck-at-algorithms-96178d389a83
'''
class Node:
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right= None
    
    
class Prob:
    @staticmethod
    def largestInBST(root):
        if root.right == None:
            return root
        print("root.val: ", root.val)
        return Prob.largestInBST(root.right)
    
    @staticmethod
    def secondLargestInBST(root):
        if root.left != None and root.right == None:
            return Prob.largestInBST(root.left)
        
        if root.right != None and root.right.right == None and root.right.left == None:
            return root
        
        return Prob.secondLargestInBST(root.right)
    
    @staticmethod
    def test1():
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.right.right = Node(20)
        #res = Prob.largestInBST(root)
        res = Prob.secondLargestInBST(root)
        print("test1 res: ", res.val)
    
    @staticmethod
    def test2():
        root = Node(10)
        root.right = Node(15)
        root.right.right = Node(20)
        root.right.right.left = Node(17)
        root.right.right.right = Node(25)
        root.right.right.right.left = Node(23)
        root.right.right.right.left.right = Node(24)
        #root.right.right.right.right = Node(30)
        #res = Prob.largestInBST(root)
        res = Prob.secondLargestInBST(root)
        print("test2 res: ", res.val)

#Prob.test1()
Prob.test2()
