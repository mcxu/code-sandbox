"""
Function that takes in array of positive ints, and returns
an integer representing max sum of non-adjacent elements in array.
Return 0 if sum cannot be generated.

Sample input: [75, 105, 120, 75, 90, 135]
Sample output: 330 (75, 120, 135)
"""

class MS:
    """
    inclPrev: max sum including previous element
    exclPrev: max sum excluding previous element
    """
    @staticmethod
    def maxSubsetSumNoAdjacent(array):
        if not array:
            return 0

        inclPrev = array[0]
        exclPrev = 0

        for i in range(1, len(array)):
            v = array[i]
            print("i={}, v={}".format(i,v))
            inclPrevPrevIter = inclPrev
            exclPrevPrevIter = exclPrev
            print("inclPrevPrevIter: {}, exclPrevPrevIter: {}".format(inclPrevPrevIter, exclPrevPrevIter))
            inclPrev = (exclPrev + v)
            exclPrev = max(inclPrevPrevIter, exclPrevPrevIter)
            print("inclPrev: {}, exclPrev: {}".format(inclPrev, exclPrev))
        
        return max(inclPrev, exclPrev)
            
    @staticmethod
    def test_maxSubsetSumNoAdjacent():
        a = [75, 105, 120, 75, 90, 135]
        MS.maxSubsetSumNoAdjacent(a)
    
    @staticmethod
    def test_maxSubsetSumNoAdjacent2():
        a = [1, 15, 3]
        max = MS.maxSubsetSumNoAdjacent(a)
        print("max: ", max)

#MS.test_maxSubsetSumNoAdjacent()
MS.test_maxSubsetSumNoAdjacent2()