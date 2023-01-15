'''
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
'''
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        pass

class Solution_BruteForce:
    def maxRepOpt1(self, text: str) -> int:
        textArr = list(text)
        maxLen = 0
        for i in range(len(textArr)-1):
            for j in range(i+1, len(textArr)):
                textArr[i],textArr[j]=textArr[j],textArr[i]
                llrs = self.getLenOfLongestRepeatingSubstring("".join(textArr))
                if llrs > maxLen:
                    maxLen = llrs
                textArr[i],textArr[j]=textArr[j],textArr[i]
        return maxLen
    
    def getLenOfLongestRepeatingSubstring(self, text):
        i = 1
        llStr = 1
        maxLen = llStr
        while i < len(text):
            curr = text[i]
            prev = text[i-1]
            
            if curr==prev:
                llStr += 1
            else:
                llStr = 1
                
            if llStr > maxLen:
                maxLen = llStr
            i+=1
        return maxLen