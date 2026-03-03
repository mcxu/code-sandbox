'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or len(s) == 1:
            return s
        
        down = True # True means going down, False means going right-up
        aux = [["" for _ in range(int(len(s)/2)+1)] for _ in range(numRows)]
        print("aux initial")
        for row in aux:
            print("auxrow: ", row)
        YMAX = numRows - 1
        i = 0
        y = 0
        x = 0
        while i < len(s):
            if down == True:
                aux[y][x] = s[i]
                y += 1
                if y == YMAX:
                    down = False
            elif down == False:
                aux[y][x] = s[i]
                x += 1
                y -= 1
                if y == 0:
                    down = True
            i += 1
        
        # aux after filling
        print("aux after filling")
        for row in aux:
            print("auxrow: ", row)
        
        # construct string
        convertedStr = ""
        for row in aux:
            convertedStr += ("".join(row))
        
        return convertedStr
    
    
    def test1(self):
        #s = "PAYPALISHIRING"
        s = "ABC"
        numRows = 2
        cs = self.convert(s, numRows)
        print("test 1 cs: ", cs)

sol = Solution()
sol.test1()
