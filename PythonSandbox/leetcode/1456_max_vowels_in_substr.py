'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        validVowels = set(['a', 'e', 'i', 'o','u'])
        maxVowelsSoFar = 0
        numVowels = 0
        
        substr = s[:k]
        #print("substr init: ", substr)
        for i in range(len(substr)):
            if substr[i] in validVowels:
                numVowels += 1
            i += 1
        maxVowelsSoFar = numVowels
        #print("maxVowelsSoFar init: ", maxVowelsSoFar)
        i = 1
        while i <= (len(s)-k):
            substr = s[i:i+k]
            #print("substr: ", substr)
            if s[i-1] in validVowels:
                numVowels -= 1
            if substr[-1] in validVowels:
                numVowels += 1
            
            if numVowels > maxVowelsSoFar:
                maxVowelsSoFar = numVowels
            #print("maxVowelsSoFar: ", maxVowelsSoFar)
            i += 1
        
        return maxVowelsSoFar
            