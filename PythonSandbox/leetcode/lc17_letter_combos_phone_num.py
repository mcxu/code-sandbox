# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        m = {'2': ['a','b','c'],
             '3': ['d','e','f'],
             '4': ['g','h','i'],
             '5': ['j','k','l'],
             '6': ['m','n','o'],
             '7': ['p','q','r','s'],
             '8': ['t','u','v'],
             '9': ['w','x','y','z']}
        
        combinations = set()
        currCombo = ""
        i = 0
        self.helper(digits, i, m, currCombo, combinations)
        return combinations
        
    def helper(self, digits, i, m, currCombo, combinations):
        if i > len(digits)-1:
            if currCombo and currCombo not in combinations:
                combinations.add(currCombo)
            return
        
        currDigit = digits[i]
        charsForDigit=m[currDigit]
        
        for _,ch in enumerate(charsForDigit):
            self.helper(digits, i+1, m, currCombo + ch, combinations)

