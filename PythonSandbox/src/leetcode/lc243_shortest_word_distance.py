'''
https://www.programcreek.com/2014/08/leetcode-shortest-word-distance-java/
Given a list of words and two words word1 and word2, 
return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.
'''

class Solution:
    def shortestDistance(self, words, word1, word2):
        dist = float('inf')
        p1 = -1
        p2 = -1
        for i,word in enumerate(words):
            if word == word1:
                p1 = i
            elif word == word2:
                p2 = i

            if p1!=-1 and p2!=-1:
                dist = min(dist, abs(p2-p1))

        return dist

    def shortestDistance2(self, words, word1, word2):
        indexMap = {}
        for i,word in enumerate(words):
            if word in indexMap.keys():
                indexMap[word].append(i)
            else:
                indexMap[word] = [i]

        dist = float('inf')
        for j in indexMap[word1]:
            for k in indexMap[word2]:
                dist = min(dist, abs(j-k))
        return dist
    
    def test1(self, alg):
        words = ["practice", "makes", "perfect", "coding", "makes"]
        #word1 = "coding"; word2 = "practice"
        word1 = "makes"; word2 = "coding"
        res = alg(words, word1, word2)
        print("res: ", res)

sol = Solution()
sol.test1(sol.shortestDistance)

