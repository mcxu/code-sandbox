"""
This problem was asked by Facebook. [Medium]
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import time

class DCP7:
    # def char2num(self, char):
    #     return ord(char) - 96
    
    # def num2char(self, num):
    #     return chr(int(num) + 96)

    # msg is a string of integers,'lll' for example
    def numWaysDecoded(self, msg):
        
        def helper(msg, i):
            print(">> i =",i)
            if i==0 or i == 1:
                return 1
            if i == 2:
                print("i is 2")
                if int(msg[:i]) < 26:
                    print("A")
                    return 2
                else:
                    print("B")
                    return 1
            
            numWays = helper(msg, i-1)
            substr = msg[i-2:i]
            print("substr: {}".format(substr))
            if i >= 2 and int(substr) < 26:
                numWays += helper(msg, i-2)
            
            return numWays
            
        return helper(msg, len(msg))

    def test1(self):
        #msg = '111' # should be 3 (1,1,1 and 1,11 and 11,1)
        #msg = '1111' # should be 5
        #msg = '3317' # should be 2 (3,3,1,7 and 3,3,17)
        msg = '11313231322' # returns 48
        numWays = self.numWaysDecoded(msg)
        print("test1: numWays: {}".format(numWays))

    '''
    Dynamic programming recursive.
    '''
    def numWaysDecodedDPRecursive(self, msg):
         
        def helperMemo(msg, i, memo):
            
            if i == 0 or i == 1:
                return 1
            if i == 2:
                if int(msg[:i]) < 26:
                    return 2
                else:
                    return 1
            
            numWays = helperMemo(msg, i-1, memo)
            
            if i >= 2 and int(msg[i-2:i]) < 26:
                numWays += helperMemo(msg, i-2, memo)
            memo[i] = numWays
            
            return memo[i]
        
        memo = {}
        return helperMemo(msg, len(msg), memo)

    def test2(self):
#         msg = '111'
#         msg = '1111'
#         msg = '1337'
        msg = '11313231322' # should return 48
        numWays = self.numWaysDecodedDPRecursive(msg)
        print("test2: numWays: {}".format(numWays))

    
    '''
    Dynamic programming iterative.
    '''
    def numWaysDecodedDPIterative(self, msg):
        numWays = [0] * (len(msg)+1)
        numWays[0] = 1
        if len(msg) == 0:
            return 1
        numWays[1] = 1
        if len(msg) == 1:
            return 1
        print("numWays init: ", numWays)
        for i in range(2, len(msg)+1):
            numWays[i] = numWays[i-1]
            if int(msg[i-2:i]) < 26:
                numWays[i] += numWays[i-2]
        print("numWays after: ", numWays)
        return numWays[-1]
            
    
    def test3(self):
        #msg = '111'
        msg = '11313231322'
        #msg = '1727271111111147281938882228228382282834321231240069494'
        numWays = self.numWaysDecodedDPIterative(msg)
        print("test3: numWays: {}".format(numWays))

def main():
    sol = DCP7()
    #sol.test_char_num_functions()
    #sol.test1()
    #sol.test2()
    sol.test3()

if __name__ == "__main__":
    main()