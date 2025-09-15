'''
Autocomplete
https://www.youtube.com/watch?v=QGVCnjXmrNg&t=376s (0:31)
Given array of words (strings), create an autocomplete system. When user inputs some prefix,
the system should return all words that contain that prefix.

Let 
'''

class ACP:
    def __init__(self):
        self.trieRoot = {}
        self.wordList = []
        
        # for test
        self.testList1 = ['dog', 'dark', 'cat', 'door', 'dodge', 'do']
        self.testList2 = ['add', 'adder', 'added', 'addition', 'adverse', 'abstain', 'abstract', 'abstraction']
        
    def buildTrie(self, wordList):
        for i in range(len(wordList)):
            word = wordList[i]
            
            node = self.trieRoot
            for j in range(len(word)):
                char = word[j]
                if char not in node.keys():
                    node[char] = {}
                node = node[char]
        return self.trieRoot
    
    def test_buildTrie(self):
        tr = self.buildTrie(self.testList1)
        print("trie built:")
        for key in tr.keys():
            print("{}: {}".format(key, self.trieRoot[key]))
    
    # pref is prefix, this function searches the trie
    def autocomplete(self, pref):
        results = []
        if pref in self.wordList:
            results.append(pref)
        
        node = self.trieRoot
        for i in range(len(pref)):
            char = pref[i]
            if char in node.keys():
                node = node[char]
            else:
                return results
            
        self.helper(node, pref, results) # do DFS
        return results
    
    # do DFS
    def helper(self, node, word, results):
        if node == {}:
            results.append(word)
            return 
        
        for key in node.keys():
            self.helper(node[key], word+key, results)
            
    
    def test_autocomplete(self):
        self.buildTrie(self.testList1)
        results = self.autocomplete("do")
        print("test autocomplete results: ", results)
    
    def test1(self):
        self.buildTrie(self.testList2)
        print("trie: ", self.trieRoot)
        results = self.autocomplete("abs")
        print("test1.1 ", results)
        results = self.autocomplete("adde")
        print("test1.2: ", results)
        results = self.autocomplete("w")
        print("test1.3: ", results)
        
sol = ACP()
#sol.test_buildTrie()
#sol.test_autocomplete()
sol.test1()

