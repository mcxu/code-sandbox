from typing import List
from utils.binary_tree_utils import TreeNode

class BTLevelOrder:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levelMap = {}
        self.traverse(root, 0, levelMap)
        return list(levelMap.values())

    def traverse(self, root, depth, levelMap):
        if not root:
            return
        
        if depth in levelMap:
            levelMap[depth].append(root.val)
        else:
            levelMap[depth] = [root.val]
        
        self.traverse(root.left, depth+1, levelMap)
        self.traverse(root.right, depth+1, levelMap)