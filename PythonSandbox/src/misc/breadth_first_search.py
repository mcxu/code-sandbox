"""
Breath first search
Implement BFS on a Node class. You may add new properties/methods,
but do not change existing ones other than breadthFirstSearch().
Parameter 'array' is an input array, it needs to be populated through BFS.

Sample input: 
        A
     / |  \
    B  C   D
   / \    / \
  E  F   G  H
    /\   \
   I J   K
   
Sample output: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        self.queue = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        if self == None:
            return array
        
        self.queue.insert(0, self)
        while self.queue:
            currNode = self.queue.pop()
            
            array.append(currNode.name)
            
            for childNode in currNode.children:
                self.queue.insert(0, childNode)
        
        return array


class Test:
    @staticmethod
    def tree1():
        tree = Node("A")
        tree.addChild("B").addChild("C").addChild("D")
        tree.children[0].addChild("E").addChild("F")
        tree.children[2].addChild("G").addChild("H")
        tree.children[0].children[1].addChild("I").addChild("J")
        tree.children[2].children[0].addChild("K")
        return tree
    
    @staticmethod
    def test1():
        tree = Test.tree1()
        array = tree.breadthFirstSearch([])
        print("test1: array: ", array)

Test.test1()
        