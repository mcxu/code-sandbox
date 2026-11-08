class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        result = False
        for y in range(len(board)):
            for x in range(len(board[0])):
                result = self.dfs(board, word, 0, y, x)
                if result:
                    return result
        return result
    
    def dfs(self, board, word, wordIdx, y, x):
        if not(0 <= y < len(board)) or not(0 <= x < len(board[0])):
            return False

        if wordIdx < len(word) and word[wordIdx] != board[y][x]:
            return False

        if wordIdx >= len(word)-1:
            return True

        swappedChar = board[y][x]
        board[y][x] = "*"

        up = self.dfs(board, word, wordIdx+1, y-1, x)
        down = self.dfs(board, word, wordIdx+1, y+1, x)
        left = self.dfs(board, word, wordIdx+1, y, x-1)
        right = self.dfs(board, word, wordIdx+1, y, x+1)
        wordExists = up or down or left or right

        board[y][x] = swappedChar

        return wordExists
        
    def test1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        result = self.exist(board, word)
        print("result: ", result)
        expected = True
        assert result == expected
    
    def test2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        result = self.exist(board, word)
        print("result: ", result)
        expected = False
        assert result == expected

if __name__ == "__main__":
    s = Solution()
    # s.test1()
    s.test2()
    