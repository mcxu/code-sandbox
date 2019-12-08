"""
Function that takes in array of positive ints, and returns
an integer representing max sum of non-adjacent elements in array.
Return 0 if sum cannot be generated.

Sample input: [75, 105, 120, 75, 90, 135]
Sample output: 330 (75, 120, 135)
"""

class MS:
    @staticmethod
    def maxSubsetSumNoAdjacent(array):
        # record the index:value of the original array
        indexMap = {}
        for i,v in enumerate(array):
            indexMap[i] = v
        print("indexMap filled:", indexMap)

        aSorted = sorted(array)
        print("aSorted:", aSorted)

    @staticmethod
    def test_maxSubsetSumNoAdjacent():
        a = [75, 105, 120, 75, 90, 135]
        MS.maxSubsetSumNoAdjacent(a)

MS.test_maxSubsetSumNoAdjacent()