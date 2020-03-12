'''
Number of steps required to convert binary number to zero

Given input string of binary chars {0,1}, determine the number of steps
required to convert this binary number to 0. A "step" is defined as such:
    Either: For even number, divide by 2.
    Or: For odd number, subtract 1.

Sample input: '1010'
Sample output: 5

Sample input: '10110'
Sample output: 7

https://www.youtube.com/watch?v=hKdd6abgj_M&feature=youtu.be
'''

class Prob:
    '''
    Time complexity: O(n), where n is the number of binary digits, since while loop goes through all n digits.
    Space complexity: O(1), since count stores the count so far for some substring of the binary number.
    '''
    @staticmethod
    def getSteps(binStr):
        
        count = 0
        
        while(int(binStr,2) > 0):
            print("binStr: ", binStr)
            # if the LSB (rightmost bit) is 0, then binStr is Even
            if binStr[-1] == '0':
                # right shift: divide by 2
                binNum = int(binStr, 2)
                binStr = bin(binNum >> 1) 
            # if the LSB is 1 then binStr is Odd
            elif binStr[-1] == '1':
                # substract 1
                binNum = int(binStr, 2)-0b1
                binStr = bin(binNum)
            count += 1
        print("binStr last updated: ", binStr)
        return count
    
    @staticmethod
    def test1():
        binStr = '1010'
        count = Prob.getSteps(binStr)
        print("test1 count: ", count)
        
    @staticmethod
    def test2():
        binStr = '10110'
        count = Prob.getSteps(binStr)
        print("test2 count: ", count)

    @staticmethod
    def test3():
        binStr = '10110111110101010101000111110001010011101111010101000100100101111010001'
        count = Prob.getSteps(binStr)
        print("test3 count: ", count)

#Prob.test1()
#Prob.test2()
Prob.test3()
            