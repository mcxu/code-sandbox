class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        keypad = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        results = []
        self.dfs(digits, 0, keypad, [], results)
        return results

    def dfs(self, digits, digitIdx, keypad, currPath, results):
        if digitIdx == len(digits):
            results.append("".join(currPath))
            return
        
        currDigit = digits[digitIdx]
        letters = keypad[currDigit]
        for letter in letters:
            currPath.append(letter)
            self.dfs(digits, digitIdx+1, keypad, currPath, results)
            currPath.pop()
        return
    
    def test1(self):
        digits = "23"
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        result = self.letterCombinations(digits)
        print("result: ", result)
        assert result == expected

if __name__ == "__main__":
    s = Solution()
    s.test1()
