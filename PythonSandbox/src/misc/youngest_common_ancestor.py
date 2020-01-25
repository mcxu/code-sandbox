'''
Youngest common ancestor
Given 3 instances of a class that have an ancestor property pointing to their youngest ancestor.
The 1st input is the top ancestor in an ancestral tree (the only instance that has no ancestor).
The other 2 inputs are descendants in the ancestral tree. Write function that returns the 
youngest common ancestor to the 2 descendants.

Sample input: Given ancestral tree (below) input Node A, Node E, Node I
       A
     /  \
    B    C
   / \  / \
  D  E F   G
 / \
H  I

Sample output: Node B
'''

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None
        
class YCA:
    @staticmethod
    def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
        return YCA.helper(topAncestor, descendantOne, descendantTwo, [], [])
    
    @staticmethod
    def helper(topAncestor, descendantOne, descendantTwo, d1List, d2List):
#         print("[1] top: {}, d1: {}, d2: {}".format(topAncestor.name, descendantOne.name, descendantTwo.name))
#         print("    d1List: ", [n.name for n in d1List])
#         print("    d2List: ", [n.name for n in d2List])

        if descendantOne in d2List:
            return descendantOne
        else:
            d1List.append(descendantOne)
            
        if descendantTwo in d1List:
            return descendantTwo
        else:
            d2List.append(descendantTwo)
        
        if descendantOne.ancestor != None:
            return YCA.helper(topAncestor, descendantOne.ancestor, descendantTwo, d1List, d2List)
        
        if descendantTwo.ancestor != None:
            return YCA.helper(topAncestor, descendantOne, descendantTwo.ancestor, d1List, d2List)

        return topAncestor

    @staticmethod
    def sampleTree():
        # make nodes
        ANode = AncestralTree("A") # top
        BNode = AncestralTree("B")
        CNode = AncestralTree("C")
        DNode = AncestralTree("D")
        ENode = AncestralTree("E") # d1
        FNode = AncestralTree("F")
        GNode = AncestralTree("G")
        HNode = AncestralTree("H")
        INode = AncestralTree("I") # d2
        
        # assign ancestors
        BNode.ancestor, CNode.ancestor = ANode, ANode
        DNode.ancestor, ENode.ancestor = BNode, BNode
        FNode.ancestor, GNode.ancestor = CNode, CNode
        HNode.ancestor, INode.ancestor = DNode, DNode
        
        return ANode, ENode, INode
    
    @staticmethod
    def test1():
        ANode, ENode, INode = YCA.sampleTree()
        n = YCA.getYoungestCommonAncestor(ANode, ENode, INode)
        print("n.name: ", n.name)
        
    
if __name__ == '__main__':
    YCA.test1()