"""
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
"""

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        maxNum = ""

        for i in range(len(number)):
            currNum = number[i]
            if currNum == digit:
                prefix = number[:i]
                suffix = number[i+1:]
                # print(f"prefix:{prefix}, suffix:{suffix}")
                newNumStr = prefix+suffix
                maxNum = max(maxNum , newNumStr)
        
        return maxNum
