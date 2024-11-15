'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # ======================= recursive ==========================
    def levelOrder(self, root: TreeNode) -> [[int]]:
        levelMap = {} # mapping levels -> [values in the nodes]
        self.dfs(root, 0, levelMap)

        output = []
        for i in range(len(levelMap)):
            output.append(levelMap[i])
        return output


    def dfs(self, root, currLevel, levelMap):
        if root == None:
            return
        
        if currLevel not in levelMap.keys():
            levelMap[currLevel] = [root.val]
        else:
            levelMap[currLevel].append(root.val)
        
        self.dfs(root.left, currLevel+1, levelMap)
        self.dfs(root.right, currLevel+1, levelMap)
    
    # ======================= recursive ==========================
    
    def makeTree(self, nodes):

        def helper(nodes, i):
            if i > len(nodes)-1:
                return None
            
            val = nodes[i]
            if val == None:
                return None
            root=TreeNode(val)
            root.left = helper(nodes, i*2+1)
            root.right = helper(nodes, i*2+2)
            return root

        return helper(nodes, 0)

    def tree1(self):
        nodes = [3,9,20,None,None,15,7]
        root = self.makeTree(nodes)
        return root
    
    def test1(self):
        root = self.tree1()
        res = self.levelOrder(root)
        print('res: ', res)

# ================ using iterative BFS ==================

    def levelOrderIterative(self, root):
        if root == None:
            return []
        
        return self.bfs(root)
    
    def bfs(self, root):
        q = [(root, 0)] # (node, level)
        visited = set() # nodes
        output = [] # lists of values by level
        
        while q:
            curr = q.pop(0)
            currNode = curr[0]
            currLevel = curr[1]
            
            if currNode not in visited and currNode != None:
                visited.add(currNode)
                
                if currLevel >= len(output):
                    output.append([currNode.val])
                else:
                    output[currLevel].append(currNode.val)
                    
                q.append((currNode.left, currLevel+1))
                q.append((currNode.right, currLevel+1))
        
        return output

s = Solution()
s.test1()