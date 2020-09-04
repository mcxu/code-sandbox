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
    # accepted but slow
    def palindromePairs(self, words: [str]) -> [[int]]:
        palSet = set()
        indices = []
        for i,v1 in enumerate(words[:-1]):
            for j in range(i+1, len(words)):
                v2 = words[j]
                a = v1+v2
                if a==a[::-1]:
                    indices.append([i,j])
                b = v2+v1
                if b==b[::-1]:
                    indices.append([j,i])
        return indices

    # using prefix / suffix checking.
    def palindromePairs2(self, words: [str]) -> [[int]]:
        m = {} # word: index
        for i,w in enumerate(words):
            if w not in m.keys(): m[w] = i
        #print("m: ", m)
        indices = set()
        for i,w in enumerate(words):
            #print("i={}, w:{}".format(i, w))
            for j in range(len(w)+1):
                pre = w[:j]
                preRev = pre[::-1]
                suf = w[j:]
                sufRev = suf[::-1]
                #print("pre: {}, suf: {}".format(pre, suf))
                
                # check that reversed suffix is in wordMap given that prefix is a palindrome, 
                # since this palindrome is the reversed suffix prepended to the word.
                if pre==pre[::-1]:
                    if sufRev in m.keys() and m[sufRev]!=i:
                        indices.add((m[sufRev], i))
                        
                # check that the reversed prefix is in wordMap, given that suffix is a palindrome,
                # since this palindrome is the reversed prefix appended to the word.
                if suf==suf[::-1]:
                    if preRev in m.keys() and m[preRev]!=i:
                        indices.add((i, m[preRev]))
        return list(indices)

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
alg = s.palindromePairs
#s.test1(alg)
#s.test2(alg)
#s.test3(alg)
s.test4(alg)