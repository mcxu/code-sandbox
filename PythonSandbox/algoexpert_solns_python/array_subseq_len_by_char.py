'''
Length of subsequences by first and last appearance of same character in array.
(intersecting spans of characters are counted as in the same subsequence.)

Example:
input: ['a','b','c','a','c','d','d']
output: [5,2]
The 5 is from index 0 to index 4. The 2 is from index 5 to index 6.
Character at index 4 is 'c'; the span 'c' - 'c' from indices 2-4 intersects
span of 'a'-'a', so the complete subsequence is 'a' - 'c' from indices 0 - 4.
'''
class Prob:
    @staticmethod
    def subseqLengthCharSpan(inputList):
        charMap = {}
        for i in range(len(inputList)):
            char = inputList[i]
            if char in charMap.keys():
                charMap[char].append(i)
            else:
                charMap[char] = [i]
        print("charMap: ", charMap)

        out = [] # list of lengths of subsequences
        loInd = 0
        hiInd = 0
        for i in range(len(inputList)):
            print("--- i= ", i)
            char = inputList[i]
            print("char: ", char)
            print("loInd: {}, hiInd: {}".format(loInd, hiInd))
            maxIndForChar = max(charMap[char])
            print("maxIndForChar: ", maxIndForChar)
            hiInd = max(hiInd, maxIndForChar)
            print("hiInd updated: ", hiInd)
            if i == hiInd:
                print("i == hiInd: ", i)
                subseqLength = hiInd-loInd+1
                out.append(subseqLength)
                loInd = hiInd + 1
        return out
            
    @staticmethod
    def test1():
        #input = ['a','b','c']
        #input = ['a','b','c','a']
        input = ['a','b','c','a','c','d','d']
        #input = ['a','b','c','d','a','e','f','g','h','i','j','e']
        #input = ['z','z','c','b','z','c','h','f','i','h','i']
        out = Prob.subseqLengthCharSpan(input)
        print("out: ", out)

Prob.test1()