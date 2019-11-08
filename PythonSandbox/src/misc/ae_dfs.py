"""
Depth First Search
"""
import time 

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

        # stack list
        self.stack = []
        self.currChildren = None

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # need to populate input array
    def depthFirstSearchIterative(self, array):
        if not self.children:
            return array

        # push a name onto stack
        self.stackPush(self)
        print("pushed Item on stack: ", self.stack)
        print("starting item: {}, with name: {}".format(self.stack[0], self.stack[0].name))

        while(self.stack):
            print("--- top of while loop ---")
            poppedNode = self.stackPop()
            self.currChildren = poppedNode.children
            poppedName = poppedNode.name
            print("poppedName:", poppedName)

            # put name on array if not visited
            if poppedName not in array:
                array.append(poppedName)
                print("elt added to array:", array)
            
            # add un-visited immediate children to stack
            """
            Need to do a pre-order traversal. However, children need to be placed
            on the stack such that they get taken off left to right. So they need
            to be put on right to left, which is why the for loop counts downwards
            in the list of children for some given node.
            """
            for i in range(len(self.currChildren)-1, -1, -1):
                childNode = self.currChildren[i]
                childName = childNode.name
                print("childName:", childName)
                if childName not in array:
                    self.stackPush(childNode)
                    print("unvisited child added to stack:", self.stack)
            
            #time.sleep(.25)
        del self.stack
        return array


    def depthFirstSearchRecursive(self, array):
        array.append(self.name)
        for childNode in self.children:
            #print("childNode:", childNode.name)
            childNode.depthFirstSearchRecursive(array)
        return array


    def stackPush(self, name):
        self.stack.append(name)
    
    def stackPop(self):
        return self.stack.pop()

class Test:
    # The one given in prompt
    def promptTree(self):
        tree = Node("A")
        tree.addChild("B").addChild("C").addChild("D")
        print("{} {} {}".format(tree.children[0].name, tree.children[1].name, tree.children[2].name))
        tree.children[0].addChild("E").addChild("F") # from B
        tree.children[0].children[1].addChild("I").addChild("J") # from F
        tree.children[2].addChild("G").addChild("H") # from D
        tree.children[2].children[0].addChild("K") # from G
        return tree
    
    def testTree1(self):
        test1 = Node("A")
        test1.addChild("B").addChild("C")
        test1.children[0].addChild("D")
        return test1
    
    def testTree5(self):
        test5 = Node("A")
        test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
        test5.children[0].addChild("E").addChild("F").addChild("O")
        test5.children[1].addChild("P")
        test5.children[2].addChild("G").addChild("H")
        test5.children[0].children[0].addChild("Q").addChild("R")
        test5.children[0].children[1].addChild("I").addChild("J")
        test5.children[2].children[0].addChild("K")
        test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
        test5.children[4].children[0].addChild("W").addChild("X")
        test5.children[4].children[0].children[1].addChild("Y").addChild("Z")
        return test5

    def test_depthFirstSearchIterative_prompt(self):
        tree = self.promptTree()
        array = []
        result = tree.depthFirstSearchIterative(array)
        print("test_depthFirstSearchIterative_Given: result: ", result)

    def test_depthFirstSearchIterative1(self):
        tree = self.testTree1()
        array = []
        result = tree.depthFirstSearchIterative(array)
        print("test_depthFirstSearchIterative2: result: ", result)

    def test_depthFirstSearchIterative5(self):
        tree = self.testTree5()
        result = tree.depthFirstSearchIterative([])
        print("test_depthFirstSearchIterative5: result: ", result)
        ans = ["A", "B", "E", "Q", "R", "F", "I", "J", "O", "C", "P", "D", "G", "K", "H", "L", "M", "S", "W", "X", "Y", "Z", "T", "U", "V"]
        if result == ans:
            print("test_depthFirstSearchIterative5: result matches answer!")

    def test_depthFirstSearchRecursive_prompt(self):
        tree = self.promptTree()
        result = tree.depthFirstSearchRecursive([])
        print("test_depthFirstSearchRecursive_prompt: result: ", result)

    def test_depthFirstSearchRecursive5(self):
        tree = self.testTree5()
        result = tree.depthFirstSearchRecursive([])
        print("test_depthFirstSearchRecursive: result: ", result)
        ans = ["A", "B", "E", "Q", "R", "F", "I", "J", "O", "C", "P", "D", "G", "K", "H", "L", "M", "S", "W", "X", "Y", "Z", "T", "U", "V"]
        if result == ans:
            print("test_depthFirstSearchRecursive: result matches answer!")

def main():
    test = Test()
    #test.testTree1()
    #test.test_depthFirstSearchIterative_prompt()
    #test.test_depthFirstSearchIterative2()
    #test.test_depthFirstSearchIterative5()
    test.test_depthFirstSearchRecursive_prompt()
    test.test_depthFirstSearchRecursive5()

if __name__ == "__main__":
    main()
