'''
Identify if 2 graphs are isomorphic.
Isomorphic: 2 graphs that have the same connections for all vertices.
'''
import time

class GNode:
    def __init__(self, name):
        self.name = name
        self.connections = [] # other GNode objects
    
    def add(self, gNode):
        self.connections.append(gNode)
        return self

class IG:
    @staticmethod
    def areGraphsIsomorphic(g1, g2):
        g1Map = IG.doBFS(g1)
        g2Map = IG.doBFS(g2)
        if g1Map == g2Map:
            return True
        return False
    
    
    @staticmethod
    def doBFS(gNode):
        # map node name to node connections names
        nodeMap = {}
        if gNode == None or len(gNode.connections) == 0:
            return nodeMap
        
        q = [gNode]
        while len(q) != 0:
            currNode = q.pop(0)
            
            nodeMap[currNode.name] = [n.name for n in currNode.connections]
            print("nodeMap: ", nodeMap)
            for n in currNode.connections:
                if n.name not in nodeMap.keys():
                    q.append(n)
        
        return nodeMap
        
    
    @staticmethod
    def areGraphsIsomorphicSimulataneous(g1, g2):
        nodeMap1 = {}
        nodeMap2 = {}
        if (g1 == None or not g1.connections) or (g2 == None or not g2.connections):
            return nodeMap1
        
        q1 = [g1]; q2 = [g2]
        while not (len(q1)==0 and len(q2)==0):
            node1 = None
            node2 = None
            
            if len(q1) != 0:
                node1 = q1.pop(0)
                nodeMap1[node1.name] = [n.name for n in node1.connections]
                
                for c in node1.connections:
                    if c.name not in nodeMap1.keys():
                        q1.append(c)
            
            if len(q2) != 0:
                node2 = q2.pop(0)
                nodeMap2[node2.name] = [n.name for n in node2.connections]
                
                for c in node2.connections:
                    if c.name not in nodeMap2.keys():
                        q2.append(c)
            
            print("nodeMap1: ", nodeMap1)
            print("nodeMap2: ", nodeMap2)
            for nodeName in nodeMap1.keys() & nodeMap2.keys(): # intersection of set-like objects
                print("    nodeName found: ", nodeName)
                if nodeMap1[nodeName] != nodeMap2[nodeName]:
                    return False

        return True
        
    
    @staticmethod
    def graph1():
        a = GNode("a"); b = GNode("b"); c = GNode("c")
        d = GNode("d"); e = GNode("e"); f = GNode("f")
        
        a.add(b).add(d).add(e)
        b.add(a).add(c)
        c.add(b).add(d)
        d.add(a).add(c).add(e)
        e.add(a).add(d).add(f)
        f.add(e)
        
        return a, c
    
    @staticmethod
    def graph2():
        a = GNode("a"); b = GNode("b"); c = GNode("c")
        d = GNode("d"); e = GNode("e"); f = GNode("f")
        
        a.add(b).add(d).add(e)
        b.add(a).add(d).add(c)
        c.add(b).add(d)
        d.add(a).add(b).add(c)
        e.add(a).add(f)
        f.add(e)
        
        return a, e
    
    @staticmethod
    def test_doBFS():
        g1 = IG.graph1()
        IG.doBFS(g1)

    @staticmethod
    def test1():
        g1,g3 = IG.graph1()
        g2 = IG.graph1()
        res = IG.areGraphsIsomorphic(g1, g3)
        print("test1: result: ", res)
    
    @staticmethod
    def test2():
        g1,g3 = IG.graph1()
        g2,g4 = IG.graph2()
        res = IG.areGraphsIsomorphic(g1, g2)
        print("test2: result: ", res)

    @staticmethod
    def test3():
        print("test3 begin")
        g1,g3 = IG.graph1()
        g2,g4 = IG.graph2()
        res = IG.areGraphsIsomorphicSimulataneous(g3, g4)
        print("test3: result: ", res)

#IG.test_doBFS()
#IG.test1()
#IG.test2()
IG.test3()

        