from typing import List

class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word: str) -> None:
        n = self.trie
        for _,c in enumerate(word):
            if c not in n.keys():
                n[c] = {}
            n = n[c]
        
        n["*"] = {}

    def search(self, word: str) -> bool:
        n = self.trie

        for i,c in enumerate(word):
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
    
def runTest(actions: List[str], words: List[List[str]]):
    trieObj = Trie()
    results = [None]

    for i in range(1, len(actions)):
        act = actions[i]
        word = words[i][0]

        match act:
            case "insert":
                result = trieObj.insert(word)
                results.append(result)
            case "search":
                result = trieObj.search(word)
                results.append(result)
            case "startsWith":
                result = trieObj.startsWith(word)
                results.append(result)
    
    return results

def test1():
    actions= ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    words =  [[],    ["apple"], ["apple"], ["app"],  ["app"],      ["app"], ["app"]]
    expected  = [None, None, True, False, True, None, True]
    results = runTest(actions, words)
    print("results: ", results)
    print("expected:", expected)
    assert results == expected

if __name__=="__main__":
    test1()