"""
This problem was asked by Facebook. [Medium]

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import string
import time

class P7:
    def char2num(self, char):
        return ord(char) - 96
    
    def num2char(self, num):
        return chr(int(num) + 96)

    # msg is a string of integers,'lll' for example
    def count_ways_decoded(self, msg):
        return self.partition_helper(msg, len(msg))

    # c: is the partition index; this iteration look at the last c values
    def partition_helper(self, msg, c):
        # gotten to end of string
        if(c == 0):
            return 1

        # index required to look at last c values
        c_ind = len(msg) - c
        if(msg[c_ind] == '0'):
            return 0

        time.sleep(.5)
        print("msg:{}, c:{}, c_ind:{}".format(msg, c, c_ind))
        sum  = self.partition_helper(msg, c-1)
        print("sum: {}".format(sum))
        if c >= 2 and int(msg[c_ind: c_ind+2]) <= 26:
            print("     msg:{}, c:{}, c_ind:{}".format(msg, c, c_ind))
            sum += self.partition_helper(msg, c-2)
            print("     sum: {}".format(sum))

        return sum

    def test_char_num_functions(self):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
        for char in chars:
            print("char2num: char: {}, num: {}".format(char, self.char2num(char)))

        nums = [1,2,3,4,5,6,7,8,9,10,26,27]
        for num in nums:
            print("num2char: num: {}, char: {}".format(num, self.num2char(num)))


    def test_count_ways_decoded(self):
        msg = '1111'
        num_ways = self.count_ways_decoded(msg)
        print("test_count_ways_decoded: num_ways: {}".format(num_ways))

def main():
    p7 = P7()
    #p7.test_char_num_functions()
    p7.test_count_ways_decoded()

if __name__ == "__main__":
    main()