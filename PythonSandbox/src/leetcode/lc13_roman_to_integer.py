'''
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

class Solution:
    '''
    Trick: go backwards instead of forwards.
    Let n = len(s)
    Time complexity: O(n), since n elements are iterated through.
    Space complexity: O(1), since tot stores the sum so far during the iteration of each char.
        (Assuming that rti map can be ignored, since that is necessary for this algorithm to work.)
    '''
    def romanToInt(self, s: str) -> int:
        rti = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        tot = 0

        i = len(s)-1
        while i >= 0:
            currChar = s[i]
            charToLeft = s[i-1]

            if i-1 < 0:
                tot += rti[currChar]
                break
            
            if rti[charToLeft] >= rti[currChar]:
                tot += rti[currChar]
            else:
                diff = rti[currChar] - rti[charToLeft]
                tot += diff
                i -= 1
                
            i -= 1
        
        return tot
        
    def test1(self):
        #s = "MCMXCIV" # 1994
        #s = "XI"
        #s = "IX"
        #s = "IV"
        s = "LVIII" # 58
        tot = self.romanToInt(s)
        print("test1 tot: ", tot)
        
sol = Solution()
sol.test1()

                