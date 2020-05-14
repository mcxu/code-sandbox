'''
https://leetcode.com/problems/string-compression/
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.
Could you solve it using only O(1) extra space?
'''

class Solution:
    def compress(self, chars) -> int:
        charsOrigLen = len(chars)
        count = 1
        lo = 0
        hi = 0
        i = 0
        while i < len(chars)-1:
            #print("--- i=",i)
            char = chars[i]
            nextchar = chars[i+1]
            if char == nextchar:
                count += 1
                hi += 1
                #print("hi updated: ", hi)
            else:
                # create comperessed substring
                compressedSubstr = chars[hi] + str(count)
                #print("compressedSubstr: ", compressedSubstr)
                #print("lo: {}, hi: {}".format(lo, hi))

                j = lo
                while j <= hi:
                    chars[j] = compressedSubstr[j-lo]
                    #print("A j: ",j)
                    j += 1
                
                i = j-1
                #print("* i=", i)
                # reset count
                count = 1
                lo = j
                hi = lo
                #print("lo updated: {} and hi updated: {}".format(lo, hi))

            #print("count: ", count)
            i += 1

        # print("chars: ", chars)
        # print("count after while: ", count)
        # print("i after while= ",i)
        # print("lo: {}, hi: {}".format(lo, hi))

        compressedSubstr = chars[hi] + str(count)
        chars = chars[:lo]
        for j in range(len(compressedSubstr)):
            chars.append(compressedSubstr[j])
        print("chars final: ", chars)

        if len(chars) < charsOrigLen:
            return len(chars)

        return charsOrigLen

    def test1(self):
        arr = ["a","a","b","b","c","c","c"]
        #arr= ["a","a","b","c","c","c"]
        #arr = ["a","b","c"]
        arr = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        res=self.compress(arr)
        print("test1 res: ", res)

s = Solution()
s.test1()

