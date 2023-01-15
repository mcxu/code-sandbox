'''
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
'''

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        m = {}
        self.serBfs(root, m)
        s = str(m)
        print("s: ", s)
        return s
        
    def serBfs(self, root, m):
        if root == None:
            return
        
        if root.val not in m.keys():
            m[root.val] = {}
        
        for c in root.children:
            m[root.val][c.val] = {}
            self.serBfs(c, m[root.val])
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        m = {} # deserialized tree, store in map
        i = 0
        self.desHelper(data, m, i)
        return m
        
    def desHelper(self, data, m, i, c=0):
        if data[i]=="{" and data[i+1]=="}":
            print("base case reached")
            return
        if m==None:
            return

        s = ["{"] # stack
        iprime = i+1
        parentIdx = None
        while s:
            print("i={}, iprime={}, iprime val:{}".format(i, iprime, data[iprime]))
            print(" stack: ", s)
            print(" m: ", m)
            if data[iprime]=="{":
                s.append(data[iprime])
                if len(s)>1:
                    self.desHelper(data, m[int(data[parentIdx])], iprime, c+1)
                    iprime = parentIdx
            elif data[iprime].isalnum():
                if len(s)==1:
                    m[int(data[iprime])] = {}
                    parentIdx = iprime
                    print(" parent set to: {}, with val: {}".format(parentIdx, data[parentIdx]))
            elif data[iprime]=="}":
                if s and s[-1]=="{":
                    s.pop()
            iprime += 1


    def test_deserialize(self):
        #dataTree = {1:{}, 2:{}, 3:{}}
        #dataTree = {1: {3: {}, 2:{}, 4:{}}}
        #dataTree = {1: {3: {5:{}, 6:{}}, 2:{7:{}, 8:{ 9:{}, 10:{}}}, 4:{}}}
        dataTree = {1: {3: {5:{}, 6:{}}}}  
        #dataTree = {1: {3: {}}}
        #dataTree = {1:{}}
        data = str(dataTree)
        print("data: ", data)
        print("data len: ", len(data))
        for d in data:
            print(d, end="\t")
        print("")
        for j in range(len(data)):
            print(str(j), end="\t")
        print("")
        res = self.deserialize(data)
        print("res: ", res)

c = Codec()
c.test_deserialize()