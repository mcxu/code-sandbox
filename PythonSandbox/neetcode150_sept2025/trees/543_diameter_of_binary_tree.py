# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional
from utils.binary_tree_utils import BinaryTreeUtils, TreeNode

class DiameterBT:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, maxDiameter = self.getHeight(root, 0)
        # print("maxHeight: ", maxHeight)
        # print("maxDiameter: ", maxDiameter)
        return maxDiameter

    def getHeight(self, root, maxDiameter):
        # print("----")
        if not root:
            return 0, 0

        leftHeight, leftDiameter = self.getHeight(root.left, maxDiameter)
        rightHeight, rightDiameter = self.getHeight(root.right, maxDiameter)

        # print("leftHeight: ", leftHeight)
        # print("rightHeight: ", rightHeight)
        # print("leftDiameter: ", leftDiameter)
        # print("rightDiameter: ", rightDiameter)

        currDiameter = leftHeight + rightHeight
        # print("currDiameter: ", currDiameter)

        maxDiameterFromCurrNode = max(currDiameter, leftDiameter, rightDiameter)
        maxDiameter = max(maxDiameter, maxDiameterFromCurrNode)

        return 1 + max(leftHeight, rightHeight), maxDiameter


    def test1(self):
        treeArr = [1,2,3,4,5]
        root = BinaryTreeUtils.buildTree(treeArr)
        dia = self.diameterOfBinaryTree(root)
        print("dia: ", dia)
        assert dia == 3
    
    def test2(self):
        treeArr = [3,1,None,None,2]
        root = BinaryTreeUtils.buildTree(treeArr)
        dia = self.diameterOfBinaryTree(root)
        print("dia: ", dia)
        assert dia == 2

    def test3(self):
        treeArr = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
        root = BinaryTreeUtils.buildTree(treeArr)
        BinaryTreeUtils.printBT(root)
        dia = self.diameterOfBinaryTree(root)
        print("test3 dia: ", dia)
        assert dia == 8

if __name__ == "__main__":
    c = DiameterBT()
    # c.test1()
    #c.test2()
    c.test3()