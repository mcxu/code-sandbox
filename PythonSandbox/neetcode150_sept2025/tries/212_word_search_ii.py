from typing import List
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.word = None  # stores complete word when this node ends a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        foundWords = []

        for i in range(len(words)):
            word = words[i]
            # print("word to search: ", word)
            if not word:
                continue

            firstChar = word[0]
            wordExists = False

            for y in range(len(board)):
                for x in range(len(board[y])):
                    boardChar = board[y][x]
                    if boardChar == firstChar:
                        print("firstChar found, firstChar: ", firstChar)
                        seenCells = set()
                        wordExists |= self.findWord(board, word, 0, y, x, seenCells)
                        print("wordExists: ", wordExists)
                        if wordExists:
                            foundWords.append(word)
                            break
                if wordExists:
                    break

        return foundWords
    
    def findWord(self, board, word, widx:int, y, x, seenCells):
        print("TOP: widx:", widx, "wchar:", word[widx] if widx < len(word) else widx, " y: {}, x: {}".format(y, x), " seenCells:\n", seenCells)

        if not (0<= widx <= len(word)-1):
            print("AAA: widx:", widx, "wchar:", word[widx] if widx < len(word) else widx, " y: {}, x: {}".format(y, x))
            return True

        if not (0 <= y <= len(board)-1) or not (0 <= x <= len(board[0])-1):
            print("BBB: widx:", widx, "wchar:", word[widx], " y: {}, x: {}".format(y, x))
            return False
        
        currChar = board[y][x]
        if currChar != word[widx]:
            return False
        
        coord: tuple = (y, x)
        if coord in seenCells:
            return False
        seenCells.add(coord)
        
        print("REC: widx:", widx, "wchar:", word[widx], "bchar:", board[y][x], " y: {}, x: {}".format(y, x))
        foundWordSoFar = False
        foundWordSoFar |= self.findWord(board, word, widx+1, y, x-1, seenCells) # Left 
        foundWordSoFar |= self.findWord(board, word, widx+1, y, x+1, seenCells) # Right
        foundWordSoFar |= self.findWord(board, word, widx+1, y-1, x, seenCells) # Up
        foundWordSoFar |= self.findWord(board, word, widx+1, y+1, x, seenCells) # Down
        seenCells.remove(coord)  # backtrack so other branches can reuse this cell
        return foundWordSoFar

    # ================ Using Trie (optimized) ================

    def findWordsTrie(self, board: List[List[str]], words: List[str]) -> List[str]:
        """Trie-optimized: search for ALL words in a single DFS pass over the board."""
        root = self.build_trie(words)
        results = set()
        for y in range(len(board)):
            for x in range(len(board[0])):
                self.dfs_trie(board, y, x, root, set(), "", results)
        return list(results)

    def build_trie(self, words: List[str]) -> dict:
        root = {}
        for word in words:
            if not word:
                continue
            node = root
            for c in word:
                if c not in node.keys():
                    node[c] = {}
                node = node[c]
            node["*"] = {} # mark end of word
        # print("root: ", root)
        return root

    def dfs_trie(self, board, y, x, node, seen, currResult, results):
        if not (0 <= y < len(board) and 0 <= x < len(board[0])):
            return 

        c = board[y][x] # char at current cell
        if c not in node.keys():
            return 
        coord = (y, x) # coord of current cell
        if coord in seen:
            return 

        seen.add(coord)
        currResult += c
        node = node[c]

        if "*" in node.keys():
            results.add(currResult)

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.dfs_trie(board, y + dy, x + dx, node, seen, currResult, results)

        seen.remove(coord)

 
    # ================== tests ==================s

    def func_switch(self):
        func = self.findWordsTrie
        return func

    def test_build_trie(self):
        words = ["oath","pea","eat","rain"]
        trieRoot = self.build_trie(words)
        print("trieRoot: ", trieRoot)

    def test1(self):
        board = [["o","a","a","n"],
                 ["e","t","a","e"],
                 ["i","h","k","r"],
                 ["i","f","l","v"]] 
        words = ["oath","pea","eat","rain"]
        expectedOutput = ["eat","oath"]

        # foundWord = self.findWord(board, "pea", 0, 0, 0)
        # print("foundWord: ", foundWord)
        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)
    
    def test2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        expectedOutput = []

        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)
    
    def test3(self):
        board = [["a"]]
        words = ["a"]
        expectedOutput = ["a"]

        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)
    
    def test4(self):
        board = [["o","a","b","n"],
                 ["o","t","a","e"],
                 ["a","h","k","r"],
                 ["a","f","l","v"]]
        words = ["oa","oaa"]
        expectedOutput = ["oa","oaa"]

        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)

    def test5(self):
        board = [["a","a"]]
        words = ["aaa"]
        expectedOutput = []

        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)
    
    def test6(self):
        board = [["a","b","c"],
                 ["a","e","d"],
                 ["a","f","g"]]
        words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
        # words = ["gfedcbaaa"]
        expectedOutput = ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]

        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)
    
    def test7(self):
        board = [["a","b","c"],
                 ["a","e","d"],
                 ["a","f","g"]]
        words = ["eaafgdcba","eaabcdgfa"]
        # words = ["eaafgdcba"]
        expectedOutput = ["eaabcdgfa","eaafgdcba"]

        foundWords = self.func_switch()(board, words)
        print("foundWords: ", foundWords)

        assert set(foundWords) == set(expectedOutput)

if __name__ == "__main__":
    s = Solution()
    # s.test_build_trie()
    s.test1()
    s.test2()
    s.test3()
    s.test4()
    s.test5()
    s.test6()
    s.test7()


