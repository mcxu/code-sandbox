'''
This problem was asked by Google. [Medium]

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
''' 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DCP3():
    # root is a tree object
    def serialize(self, root):
        serTree = self.serHelper(root)
        return serTree[:-1]
        # example:  root,left,left.left,right

    def serHelper(self, root):
        if root==None:
            return ""

        serStr = (str(root.val) + ",")
        left = self.serHelper(root.left)
        right = self.serHelper(root.right)
        return serStr + left + right

    # root is a string (serialized tree)
    def deserialize(self, root):
        rootSplit = root.split(",")
        rootObj = None
        if len(rootSplit) > 0:
            rootObj = Node(rootSplit[0])

        for i in range(1, len(rootSplit)):
            pathStr = rootSplit[i]
            nodesSplit = pathStr.split(".")
            self.deserHelper(nodesSplit, "", rootObj)
        
        return rootObj
    
    def deserHelper(self, nodesSplit, builtPath, rootObj):
        if not nodesSplit:
            return
        
        currNodeStr = nodesSplit.pop(0)
        #print("currNodeStr: ", currNodeStr)
        #print("nodesSplit: ", nodesSplit)
        builtPath += currNodeStr + "."
        currNode = Node(builtPath[:-1])
        
        if currNodeStr == "left":
            if not rootObj.left:
                rootObj.left = currNode
            self.deserHelper(nodesSplit, builtPath, rootObj.left)
        if currNodeStr == "right":
            if not rootObj.right:
                rootObj.right = currNode
            self.deserHelper(nodesSplit, builtPath, rootObj.right)
    
    def testSerialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        serTree = self.serialize(node)
        print("serTree: ", serTree)
    
    def testDeserialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        serTree = self.serialize(node)
        print("serTree: ", serTree)
        deserTree = self.deserialize(serTree)
        print("check deserTree ****")
        print(" root: ", deserTree.val)
        print(" root.left:", deserTree.left.val)
        print(" root.left.left:", deserTree.left.left.val)
        #print(" root.left.left.left:", deserTree.left.left.left.val) # None, no val
        print(" root.right:", deserTree.right.val)
        #print(" root.right.right:", deserTree.right.right.val) # None, no val
        reserTree = self.serialize(deserTree)
        print("reserialized: ", reserTree)
    
d = DCP3()
#d.testSerialize()
d.testDeserialize()