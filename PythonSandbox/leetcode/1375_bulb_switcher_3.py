'''
https://leetcode.com/problems/bulb-switcher-iii/
'''
class Solution:
    def numTimesAllBlue(self, light: [int]) -> int:
        m = 0
        kSum = 0
        bulbSum = 0
        for k,b in enumerate(light):
            #print("--- k: {}, b: {}".format(k, b))
            kSum += k+1
            bulbSum += b
            #print("kSum: {}, bulbSum: {}".format(kSum, bulbSum))
            if kSum==bulbSum:
                m += 1
                #print("m: ", m)
        return m