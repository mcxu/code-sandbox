'''
336. Palindrome Pairs (https://leetcode.com/problems/palindrome-pairs/)
Given a list of unique words, find all pairs of distinct indices (i, j) 
in the given list, so that the concatenation of the two words, 
i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''

class Solution:
    # Brute force solution: Time limit exceeded
    def palindromePairs(self, words):
        out = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ccs1 = words[i] + words[j]
                if self.isPal(ccs1):
                    out.append([i,j])
                ccs2 = words[j] + words[i]
                if self.isPal(ccs2):
                    out.append([j,i])
                 
        return out

    def isPal(self, word):
        for i in range(int(len(word)/2)):
            if word[i] != word[len(word)-1-i]:
                return False
        return True

    # using prefix / suffix checking.
    def palindromePairs2(self, words):
        wordMap = {} # store reverse of words -> index in input words list
        #populate map
        for i, word in enumerate(words):
            wordMap[word] = i
        print("wordMap: ", wordMap)

        out = []
        for i in range(len(words)):
            word = words[i]
            print("i={}, word: {}".format(i, word))
            for j in range(len(word)+1):
                prefix = word[:j]
                suffix = word[j:]
                print("prefix: {}, suffix: {}".format(prefix, suffix))
                prefixRev = prefix[::-1]
                suffixRev = suffix[::-1]

                # check that reversed suffix is in wordMap given that prefix is a palindrome, 
                # since this palindrome is the reversed suffix prepended to the word.
                if suffixRev in wordMap.keys() and self.isPal(prefix):
                    suffixRevInd = wordMap[suffixRev]
                    print("     suffixRevInd: ", suffixRevInd)
                    pair = [suffixRevInd, i]
                    if suffixRevInd != i and pair not in out:
                        out.append(pair)
                
                # check that the reversed prefix is in wordMap, given that suffix is a palindrome,
                # since this palindrome is the reversed prefix appended to the word.
                if prefixRev in wordMap.keys() and self.isPal(suffix):
                    prefixRevInd = wordMap[prefixRev]
                    print("     prefixRevInd: ", prefixRevInd)
                    pair = [i, prefixRevInd]
                    if prefixRevInd != i and pair not in out:
                        out.append(pair)
        return out

    def test1(self, alg):
        input = ["abcd","dcba","lls","s","sssll"]
        res = alg(input)
        print("test1 res: ", res)

    def test2(self, alg):
        input = ["bat","tab","cat"]
        res = alg(input)
        print("test2 res: ", res)
    
    def test3(self, alg):
        input = ["lls", "sssll"]
        res = alg(input)
        print("test3 res: ", res)

    def test4(self, alg):
        input = ["a",""] # Expected: [[0,1],[1,0]]
        res = alg(input)
        print("test4 res: ", res)

s = Solution()
alg = s.palindromePairs2
#s.test1(alg)
#s.test2(alg)
#s.test3(alg)
s.test4(alg)