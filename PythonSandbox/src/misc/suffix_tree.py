'''
Suffix Tree

Given a string like "babc", build a suffix tree from a class.
From the above generated tree, given a string like "abc", determine
if this string is a suffix of "babc".
'''

class SuffixTree:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.buildTree(string)
    
    def __str__(self):
        print("printing root map: ")
        for key in self.root.keys():
            print("{}: {}".format(key, self.root[key]))
        return ""

    def buildTree(self, string):
        for i in range(len(string)):
            print("i=", i)
            self._insertSubstring(i, string)

    # insert each substring, starting from the string itself, and moving to the [right:end]
    # each substring will be going down it's own "path", char-wise in the self.root map.
    def _insertSubstring(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            jChar = string[j]
            print("j={}, jChar: {}".format(j, jChar))
            #print("node.keys: ", node.keys())
            if jChar not in node.keys():
                node[jChar] = {}
            node = node[jChar]
        node[self.endSymbol] = True
        print(self)
    
    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            char = string[i]
            if char not in node.keys():
                return False
            node = node[char]
        
        # handles the case that user enters search string that is a complete non-suffix substring.
        # For example string added is qqqqwww, and the user searches for qqw
        if self.endSymbol not in node.keys():
            return False
        
        # if above if condition falls through, then you know you are at the end of a path in the map.
        return node[self.endSymbol]

def test1():
    string = "babc"
    st = SuffixTree(string)
    print("test1 adding string:", string)
    print("map after adding:\n", st)
    
    containStr = "bc"
    c = st.contains(containStr)
    print("c: ",c)
    
def test2():
    string = "qqqqwww"
    st = SuffixTree(string)
    print("test2 adding string:", string)
    print("map after adding:\n", st)
    
    containStr = "qwww"
    notContainStr = "qqw"
    c = st.contains(containStr)
    print("c: ",c)
    c = st.contains(notContainStr)
    print("c: ",c)
    
#test1()
test2()   



    
        