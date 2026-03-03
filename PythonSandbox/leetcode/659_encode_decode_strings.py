'''
659 · Encode and Decode Strings
'''

class Solution:

    def __init__(self):
        self.DELIMITER = "\\\\\\"

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encodedStr = self.DELIMITER.join(strs)
        return encodedStr

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        # decodedStr = str.split(self.DELIMITER)

        # if they ask you to do it the stupid way
        decodedStrs = []
        start = 0
        for i in range(len(self.DELIMITER), len(str)):
            window = str[i-len(self.DELIMITER): i]
            if window == self.DELIMITER:
                decodedStrs.append(str[start : i - len(self.DELIMITER)])
                start = i

        if start < len(str) and str[start:] != self.DELIMITER:
            decodedStrs.append(str[start:])

        return decodedStrs


    def test(self):
        cases = [
            dict(input = ["lint","code","love","you"], expected = ["lint","code","love","you"]),
        ]

        for case in cases:
            caseInput = case["input"]
            caseExp = case["expected"]

            encodedStr = self.encode(caseInput)
            print("encodedStr: ", encodedStr)
            decodedStrs = self.decode(encodedStr)
            print("decodedStrs: ", decodedStrs)
            
            assert decodedStrs == caseExp

sol = Solution()
sol.test()
