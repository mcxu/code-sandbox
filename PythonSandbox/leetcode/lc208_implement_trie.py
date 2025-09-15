"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/ 
"""
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        n = self.trie

        for _,c in enumerate(word):
            if c in n.keys():
                n = n[c]
            else:
                n[c] = {}
                n = n[c]
        
        n["*"] = {}

    def search(self, word: str) -> bool:
        n = self.trie
        for _,c in enumerate(word):
            if c in n.keys():
                n = n[c]
            else:
                return False

        if "*" in n.keys() or n == {}:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        n = self.trie
        for _,c in enumerate(prefix):
            if c in n.keys():
                n = n[c]
            else:
                return False
        return True
