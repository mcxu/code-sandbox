"""
Algoexpert - Easy - 2/13 
Depth First Search
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

        # stack list
        self.stack = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # need to populate input array
    # iterative solution
    def depthFirstSearch(self, array):
        if not self.children:
            return array

        # push a name onto stack
        self.stackPush(self.name)

        while(self.stack):
            pass        


        

    def stackPush(self, name):
        self.stack.append(name)
    
    def stackPop(self):
        return self.stack.pop(-1)

class Test:
    # The one given in prompt
    def testTree1(self):
        tree = Node("A")
        tree.addChild("B").addChild("C").addChild("D")
        print("{} {} {}".format(tree.children[0].name, tree.children[1].name, tree.children[2].name))
        tree.children[0].addChild("E").addChild("F") # from B
        tree.children[0].children[1].addChild("I").addChild("J") # from F
        tree.children[2].addChild("G").addChild("H") # from D
        tree.children[2].children[0].addChild("K") # from G
        

def main():
    test = Test()
    test.testTree1()

if __name__ == "__main__":
    main()
