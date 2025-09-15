'''
https://leetcode.com/problems/word-search/description/
'''

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        wordExists = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                # do dfs
                wordExists = self.dfs(board, row, col, word, 0)
                if wordExists:
                    return wordExists
        return wordExists
    
    def dfs(self, board, row, col, word, wordIdx):
        # print(f"row: {row}, col: {col}, wordIdx: {wordIdx} , word so far: {word[:wordIdx+1]}")
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or (wordIdx<len(word) and board[row][col] != word[wordIdx]):
            return False

        if wordIdx == len(word)-1 and board[row][col] == word[wordIdx]:
            return True

        # mark current char with a non-alphabetical char
        origChar = board[row][col]
        board[row][col] = '*'

        # do recursive calls
        up = self.dfs(board, row-1, col, word, wordIdx+1)
        down = self.dfs(board, row+1, col, word, wordIdx+1)
        left = self.dfs(board, row, col-1, word, wordIdx+1)
        right = self.dfs(board, row, col+1, word, wordIdx+1)

        wordExists = up or down or left or right

        # place orig char back
        board[row][col] = origChar

        return wordExists
    

    def test(self):
        cases = [
            # dict(head = [1,2,3,4], expected = [1,4,2,3]),
            dict(head = [1,2,3,4,5], expected = [1,5,2,4,3]),
            # dict(head = [1,2,3], expected = [1,3,2]),
            # dict(head = [1,2], expected = [1,2])
        ]

        for case in cases:
            caseArr = case["head"]
            caseExp = case["expected"]

            headFromCase = self.createLinkedList(caseArr)
            # caseArrFromLL = self.linkedListToArray(caseLL)
            # print("caseArrFromLL: ", caseArrFromLL)

            headFromFunc = self.reorderList(headFromCase)

            result = self.linkedListToArray(headFromFunc)
            print("result: ", result)
            assert result == caseExp