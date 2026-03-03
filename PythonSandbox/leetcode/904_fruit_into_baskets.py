""" https://leetcode.com/problems/fruit-into-baskets/description/
"""
from typing import List
# [1,0,1,4,1,4]
#  0 1 2 3 4 5
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freqMap = {}
        maxFruits = 0

        i = 0
        j = 0
        while j < len(fruits):
            jthFruit = fruits[j]
            if jthFruit not in freqMap.keys():
                freqMap[jthFruit] = 1
            else:
                freqMap[jthFruit] += 1
            
            ithFruit = fruits[i]
            if len(freqMap.keys()) > 2 and ithFruit in freqMap.keys():
                freqMap[ithFruit] -= 1

                if freqMap[ithFruit] == 0:
                    freqMap.pop(ithFruit)
                
                i += 1

            maxFruits = max(maxFruits, j - i + 1)

            j += 1

        return maxFruits

    def test(self):
        #fruits = [1,2,1] # expected: 3
        #fruits = [0,1,2,2] # expected: 3 (Can pick from [1,2,2])
        #fruits = [1,2,3,2,2] # expected: 4 (can pick from [2,3,2,2])
        fruits = [0,0,0,8,3,8,3,7,4] # expected 4
        res = self.totalFruit(fruits)
        print("res: ", res)

    def test2(self):
        #fruits = [1,0,1,4,1,4,1,2,3] # expected 5
        fruits = [1,0,1,4,1,4]

        res = self.totalFruit(fruits)
        print("res: ", res)

s = Solution()
# s.test()
s.test2()