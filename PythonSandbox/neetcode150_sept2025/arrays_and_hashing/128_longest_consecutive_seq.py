# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List

class LongestConsecutiveSequence:
    """ Let n ~ len(nums)
    TC: O(n), bc numsSet can be max len(nums) if nums has all unique numbers, and for loop iterates throught that.
        Inner while loop is less than O(n) because the prevNum condition ensures it only iterates from the first number of a consecutive sequence.
    SC: O(n), bc numsSet can be max len(nums), other prevNum and nextNum are just O(1)
    """
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        longestSoFar = 0 #longest length so far

        for n in numsSet:
            longestFromCurrNum = 1
            
            prevNum = n-1
            nextNum = n+1
            while prevNum not in numsSet and nextNum in numsSet:
                longestFromCurrNum += 1
                nextNum += 1
            
            longestSoFar = max(longestSoFar, longestFromCurrNum)
        
        return longestSoFar
            

    def test_1(self):
        testCases = [
            [[100,4,200,1,3,2], 4],
            [[0,3,7,2,5,8,4,6,0,1], 9],
            [[1,0,1,2], 3],
            [[0], 1],
            [[0,3,7,2,5,8,4,6,0,1], 9],
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
            assert output == expected


if __name__ == "__main__":
    cl = LongestConsecutiveSequence()
    cl.test_1()