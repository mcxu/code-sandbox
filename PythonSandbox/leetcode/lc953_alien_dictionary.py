"""
https://leetcode.com/problems/verifying-an-alien-dictionary/
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character 
which is less than any other character (More info).
"""

class Solution:
    def isAlienSorted2(self, words, order):
        for i in range(len(words)-1):
            currWord = words[i]
            nextWord = words[i+1]
            minLen = min(len(currWord), len(nextWord))
            for j in range(minLen):
                currCharOrder = order.index(currWord[j])
                nextCharOrder = order.index(nextWord[j])
                
                if currCharOrder != nextCharOrder:
                    if currCharOrder > nextCharOrder:
                        return False
                    break
            
            currCharOrderLast = order.index(currWord[minLen-1])
            nextCharOrderLast = order.index(nextWord[minLen-1])
            if len(currWord) > len(nextWord) and currCharOrderLast >= nextCharOrderLast:
                return False
        return True

    def isAlienSorted(self, words, order):
        wordMap = {}
        for i,word in enumerate(words):
            wordMap[i] = []
            for j in range(len(word)):
                wordMap[i].append(order.index(word[j]))

        print("wordMap: ", wordMap)

        for k in range(len(words)-1):
            currWordCharOrders = wordMap[k]
            nextWordCharOrders = wordMap[k+1]
            print("currWordCharOrders:", currWordCharOrders)
            print("nextWordCharOrders:", nextWordCharOrders)

            currLen = len(currWordCharOrders)
            nextLen = len(nextWordCharOrders)
            minLen = min(currLen, nextLen)
            print("minLen: ", minLen)
            
            idxOf1stDiff = 0
            idxSet = False
            for m in range(minLen):
                currCharOrder = currWordCharOrders[m]
                nextCharOrder = nextWordCharOrders[m]
                print("m={}, currCharOrder: {}, nextCharOrder: {}".format(m, currCharOrder, nextCharOrder))
                
                # compare characters
                if currCharOrder != nextCharOrder:
                    if currCharOrder > nextCharOrder:
                        return False
                    break
            
            if currLen > nextLen and currWordCharOrders[minLen-1] >= nextWordCharOrders[minLen-1]:
                return False

        return True

    def test1(self,alg):
        order = "hlabcdefgijkmnopqrstuvwxyz"
        words = ["hello","leetcode"]
        # expected true
        res = alg(words, order)
        print("test1 res: ", res)

    def test2(self,alg):
        order = "worldabcefghijkmnpqstuvxyz"
        words = ["word","world","row"]
        # expected false
        res = alg(words, order)
        print("test2 res: ", res)

    def test3(self,alg):
        order = "abcdefghijklmnopqrstuvwxyz"
        words = ["apple","app"] # expected false
        #words = ["app","apple"] # expected true
        res = alg(words, order)
        print("test3 res: ", res)

    def test4(self,alg):
        order = "zkgwaverfimqxbnctdplsjyohu"
        words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
        # Expected false
        res = alg(words, order)
        print("test4 res: ", res)
    
    def test5(self,alg):
        order = "ngxlkthsjuoqcpavbfdermiywz"
        words = ["kuvp","q"]
        # Expected true
        res = alg(words, order)
        print("test5 res: ", res)
        

s = Solution()
#alg = s.isAlienSorted
alg = s.isAlienSorted2

#s.test1(alg)
#s.test2(alg)       
#s.test3()
#s.test4()
s.test5(alg)