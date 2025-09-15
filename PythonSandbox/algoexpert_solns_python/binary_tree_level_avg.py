'''
Given binary tree, find the averages at all levels of the binary tree.
Return the result as an array, where the indices are levels and values are averages.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Prob:
    '''
    Recursive DFS
    Let n = number of nodes in tree, d = depth of tree
    Time complexity: O(n+d), O(n) for DFS, O(d) for iterating through levelMap.
    Space complexity: O(d), as there can be a max of d recursive function calls on the call stack.
    '''
    @staticmethod
    def btLevelAverages(root):
        
        def helper(root, depth, levelMap): # O(n) time
            if root == None:
                return root
            
            if depth not in levelMap.keys():
                levelMap[depth] = [root.val, 1]
            else:
                levelMap[depth][0] += root.val
                levelMap[depth][1] += 1
            
            helper(root.left, depth+1, levelMap)
            helper(root.right, depth+1, levelMap)
        
        levelMap = {} # stores: level: [sum of values, count of values]
        helper(root, 0, levelMap) # O(
        print("levelMap populated: ", levelMap)
        out = []
        for key in range(max(levelMap.keys())+1): # O(depth) time
            avg = float(levelMap[key][0]/levelMap[key][1])
            out.append(avg)
        
        return out
    
    '''
    Iterative BFS
    Let n = number of nodes. d = depth of tree
    Time complexity: O(n + d)
    '''
    @staticmethod
    def btLevelAveragesBFS(root):
        if root == None:
            return []
        
        q = [(root, 0)] # (node, depth)
        levelMap = {}
        maxDepth = 0
        while q:
            currNodeDepthTuple = q.pop()
            currNode = currNodeDepthTuple[0]
            currDepth = currNodeDepthTuple[1]
            
            if currDepth not in levelMap.keys():
                levelMap[currDepth] = [currNode.val, 1]
            else:
                levelMap[currDepth][0] += currNode.val
                levelMap[currDepth][1] += 1
            
            if currDepth > maxDepth:
                maxDepth = currDepth

            if currNode.left:
                q.insert(0, (currNode.left, currDepth+1))

            if currNode.right:
                q.insert(0, (currNode.right, currDepth+1))
                
        print("levelMap:", levelMap)
        print("maxDepth: ", maxDepth)
        
        out = []
        for i in range(maxDepth+1):
            out.append(float(levelMap[i][0]/levelMap[i][1]))
        return out 
    
    @staticmethod
    def test1(alg):
        root = Node(4)
        root.left = Node(7)
        root.left.left = Node(10)
        root.left.right = Node(2)
        root.left.right.right = Node(6)
        root.left.right.right.left = Node(2)
        root.right = Node(9)
        root.right.right = Node(6)
        
        ans = alg(root)
        print("ans: ", ans)

#alg = Prob.btLevelAverages
alg = Prob.btLevelAveragesBFS

Prob.test1(alg)
        