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
    def romanToInt(self, s: str) -> int:
        rti = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}
        
        tot = 0
        i = len(s)-1
        while i >= 0:
            #print("--- i={}, rnum:{}".format(i, s[i]))
            
            if i == 0:
                tot += rti[s[i]]
                break
            
            if rti[s[i]] > rti[s[i-1]]:
                # subtract
                diff = rti[s[i]] - rti[s[i-1]]
                tot += diff
                i = i-1
            else:
                # add
                tot += rti[s[i]]
            print("tot is: ", tot)
            i = i-1
                
        print("tot: ", tot)
        return int(tot)
        
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

                