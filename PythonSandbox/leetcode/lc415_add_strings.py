
'''
https://leetcode.com/problems/add-strings/
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # add appropriate zeroes to the start
        if len(num1) < len(num2):
            num1 = (len(num2)-len(num1))*"0"+num1
        elif len(num1) > len(num2):
            num2 = (len(num1)-len(num2))*"0"+num2
        #print("num1:", num1)
        #print("num2:", num2)
        
        s = 0
        multFactor = 1
        for i in range(len(num1)-1, -1, -1):
            placeSum = (int(num1[i]) + int(num2[i]))*multFactor  
            s += placeSum
            multFactor *= 10
        return str(s)