class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeUtils:
    def printBT(self, tree):
        h = self.treeHeight(tree)
        for i in range(0,h+1):
            self.printLevel(tree, i)
            print("")

    # https://www.geeksforgeeks.org/print-level-order-traversal-line-line/
    def printLevel(self, tree, treeDepth):
        if tree is None:
            return
        
        if(treeDepth == 1):
            print("{}".format(tree.val), end=' ')
        else:
            self.printLevel(tree.left, treeDepth-1)
            self.printLevel(tree.right, treeDepth-1)
    
    # root is height of 0
    def treeHeight(self, tree):
        if tree is None:
            return 0
        ld = self.treeHeight(tree.left)
        rd = self.treeHeight(tree.right) 
        if rd > ld:
            return rd+1
        else:
            return ld+1


    def test1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.left.left = TreeNode(0)

        tree.right = TreeNode(5)
        tree.right.left = TreeNode(4)
        tree.right.right= TreeNode(8)

        d = self.treeHeight(tree)
        print("depth: " + str(d))
        self.printBT(tree)

def main():
    btUtils = BinaryTreeUtils()
    btUtils.test1()

if __name__ == "__main__":
    main()