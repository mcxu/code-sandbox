from typing import List

class LongestConsecutiveSequence:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLenSoFar = 0

        for n in numsSet:
            if n-1 not in numsSet:
                maxLenCurr = 1
                nextNum = n+1

                while nextNum in numsSet:
                    maxLenCurr += 1
                    nextNum += 1
            
                maxLenSoFar = max(maxLenSoFar, maxLenCurr)
        
        return maxLenSoFar


    def test_1(self):
        testCases = [
            # [[100,4,200,1,3,2], 4],
            # [[0,3,7,2,5,8,4,6,0,1], 9],
            # [[1,0,1,2], 3],
            # [[0], 1],
            # [[0,3,7,2,5,8,4,6,0,1], 9],
            [[9,1,4,7,3,-1,0,5,8,-1,6], 7],
            [[], 0]
        ]
        
        for tc in testCases:
            nums = tc[0]
            print("TEST CASE: ", nums)
            expected = tc[1]
            print("expected: ", expected)
            output = self.longestConsecutive(nums)
            print("output: ", output)


if __name__ == "__main__":
    cl = LongestConsecutiveSequence()
    cl.test_1()