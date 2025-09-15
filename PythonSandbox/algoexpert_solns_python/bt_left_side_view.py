'''
Print left side view of binary tree from root node.
Ref: https://aonecode.com/amazon-interview-questions-software-engineer
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None

class Prob:
    '''
    Let d = tree depth, n = num of nodes in tree.
    Time complexity: O(2n), which is O(n)
        helper: O(n) since all nodes in tree are traversed recursively.
        for loop for depthMap.keys(): O(n), because the worst case is if tree is a linked list, in which case depth=n
    Space complexity: 
        O(n) worst case caused by using a depthMap (worst case is if tree is linked list)
    '''
    @staticmethod
    def btLeftSideView(root):
        depthMap = {} # stores depth: root value
        Prob.helper(root, 0, depthMap)

        leftView = []
        for depth in range(max(depthMap.keys())+1):
            leftView.append(depthMap[depth])
        return leftView

    @staticmethod
    def helper(root, depth, depthMap):
        if root == None:
            return 

        depthMap[depth] = root.value

        # traverse right, then left. Because you want leftmost node as the last node at a depth that you want to look at.
        Prob.helper(root.right, depth+1, depthMap)
        Prob.helper(root.left, depth+1, depthMap)

    @staticmethod
    def tree1():
        root = Node("A")
        root.left = Node("B")
        # for below Node B
        b = root.left
        b.left = Node("H")
        b.right = Node("C")
        b.right.right = Node("D")
        b.right.right.right = Node("E")
        b.left.left = Node("N")
        b.left.right = Node("I")
        b.left.left.right = Node("O")
        b.left.right.right = Node("J")
        # for below Node E
        e = b.right.right.right
        e.left = Node("K")
        e.right = Node("F")
        e.left.left = Node("P")
        e.left.right = Node("L")
        e.left.right.left = Node("Q")
        e.right.right = Node("G")
        e.right.right.left = Node("M")
        return root

    @staticmethod
    def test1():
        root = Prob.tree1()
        res = Prob.btLeftSideView(root)
        print("test1 res: ", res)

Prob.test1()