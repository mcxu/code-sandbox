'''
Given binary tree, return a list of node values as if you
were looking at the bottom of the tree.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None

class Prob:
    @staticmethod
    def btBottomView(root):
        xMap = {} # stores: x value: (y value, node value) tuple
        Prob.helper(root, 0, 0, xMap)
        print("xMap: ", xMap)

        minx = min(xMap.keys())
        maxx = max(xMap.keys())
        botView = []
        for x in range(minx, maxx+1):
            botVal = xMap[x][1]
            botView.append(botVal)
        return botView
    
    @staticmethod
    def helper(root, x, y, xMap):
        if root == None:
            return

        if root.value not in xMap.keys():
            xMap[x] = (y, root.value)
        else:
            item = xMap[x]
            itemy = item[0]
            if y > itemy:
                xMap[x] = (y, root.value)

        Prob.helper(root.left, x-1, y+1, xMap)
        Prob.helper(root.right, x+1, y+1, xMap)

    @staticmethod
    def tree1():
        root = Node("A")
        root.left = Node("B")
        root.left.right = Node("D")
        root.right = Node("C")
        return root

    @staticmethod
    def tree2():
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
        #root = Prob.tree1()
        root = Prob.tree2()
        res = Prob.btBottomView(root)
        print("test1 res: ", res)

Prob.test1()