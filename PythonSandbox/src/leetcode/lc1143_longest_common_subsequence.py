"""
https://www.enjoyalgorithms.com/blog/longest-common-subsequence
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        initRow = [0 for x in range(len(text1)+1)]
        subseqMatrix = [initRow.copy() for y in range(len(text2)+1)]

        #self.printMatrix(subseqMatrix)

        for y in range(1, len(text2)+1): # row
            for x in range(1, len(text1)+1): # col
                #print(f"----- y={y}, x={x} -----")
                #print(f"letters: y: {text2[y-1]}, x: {text1[x-1]}")
                if text1[x-1] == text2[y-1]:
                    subseqMatrix[y][x] = subseqMatrix[y-1][x-1] + 1
                    #print(f"subseqMatrix[{y}][{x}] set to {subseqMatrix[y][x]}")
                else:
                    subseqMatrix[y][x] = max(subseqMatrix[y][x-1], subseqMatrix[y-1][x])
                
                #self.printMatrix(subseqMatrix)
        
        return subseqMatrix[len(text2)][len(text1)]

    def printMatrix(self, m):
        print("printMatrix")
        for row in m:
            print(row)


    def test(self):
        cases = [
            # dict(text1 = "abcde", text2 = "ace", expected=3),
            # dict(text1 = "abc", text2 = "abc", expected=3),
            # dict(text1 = "abc", text2 = "def", expected=0),
            dict(text1 = "bsbininm", text2 = "jmjkbkjkv", expected=1)
        ]

        for case in cases:
            print("case: ", case)
            text1 = case["text1"]; text2 = case["text2"]
            res = self.longestCommonSubsequence(text1, text2)
            print("res: ", res)
            assert res == case["expected"]

sol = Solution()
sol.test()