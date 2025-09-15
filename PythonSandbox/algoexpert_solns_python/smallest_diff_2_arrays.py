"""
Function that takes 2 arrays. Find a pair of numbers from the arrays
(1 number from each array), whose absolute difference is closest to 0.
Assume only there only exists 1 pair of smallest difference.

Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]
"""

class SD:
    @staticmethod
    def smallestDifference(arrayOne, arrayTwo):
        sad = abs(arrayOne[0] - arrayTwo[0]) # smallest abs diff
        sadNums = None
        for i,iv in enumerate(arrayOne, start=1):
            for j,jv in enumerate(arrayTwo, start=1):
                currDiff = abs(iv-jv)
                if currDiff < sad:
                    sad = currDiff
                    sadNums = [iv, jv]
                    #print("i={}, j={}, iv: {}, jv: {}".format(i, j, iv, jv))
                    
        return sadNums
    
    @staticmethod
    def test_smallestDifference():
        one = [-1, 5, 10, 20, 28, 3]
        two = [26, 134, 135, 15, 17]
        sadNums = SD.smallestDifference(one, two)
        print("sadNums: ", sadNums)

def main():
    SD.test_smallestDifference()
    
main()