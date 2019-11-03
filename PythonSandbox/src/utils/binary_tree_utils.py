class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeUtils:
    @staticmethod
    def printBT(tree):
        h = BinaryTreeUtils.treeHeight(tree)
        for i in range(0,h+1):
            BinaryTreeUtils.printLevel(tree, i)
            print("")

    # https://www.geeksforgeeks.org/print-level-order-traversal-line-line/
    @staticmethod
    def printLevel(tree, treeDepth):
        if tree is None:
            return
        
        if(treeDepth == 1):
            print("{}".format(tree.val), end=' ')
        else:
            BinaryTreeUtils.printLevel(tree.left, treeDepth-1)
            BinaryTreeUtils.printLevel(tree.right, treeDepth-1)
    
    # root is height of 0
    @staticmethod
    def treeHeight(tree):
        if tree is None:
            return 0
        ld = BinaryTreeUtils.treeHeight(tree.left)
        rd = BinaryTreeUtils.treeHeight(tree.right) 
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

        d = BinaryTreeUtils.treeHeight(tree)
        print("depth: " + str(d))
        BinaryTreeUtils.printBT(tree)

def main():
    btUtils = BinaryTreeUtils()
    btUtils.test1()

if __name__ == "__main__":
    main()