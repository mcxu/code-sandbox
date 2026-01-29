from typing import List
from utils.binary_tree_utils import TreeNode

class BTRightSide:
    def rightSideView(self, root: TreeNode) -> List[int]:
        numMap = {}
        self.traverse(root, 0, numMap)
        output = []
        for depth in sorted(numMap.keys()):
            output.append(numMap[depth])
        return output

    def traverse(self, root, depth, numMap):
        if not root:
            return 
        
        numMap[depth] = root.val

        self.traverse(root.left, depth+1, numMap)
        self.traverse(root.right, depth+1, numMap)
    
    