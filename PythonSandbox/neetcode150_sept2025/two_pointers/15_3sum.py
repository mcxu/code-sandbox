from typing import List

class ThreeSum:
    # Non sorted solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        
        for i in range(len(nums)):
            print("======\ni: ", i)
            n = nums[i]
            print('n: ', n)
            twoSumTarget = -n # triplet must always add up to 0
            j = i+1
            if j < len(nums)-1:
                tsResult = self.twoSum(j, nums, twoSumTarget)
                print("tsResult: ", tsResult)
                if len(tsResult) > 0:
                    for double in tsResult:
                        triplet = sorted([n] + list(double))
                        triplets.add(tuple(triplet))
            else:
                break
        
        tripletsList = [list(tup) for tup in triplets]
        return tripletsList

    def twoSum(self, j, nums, target) -> set[tuple]:
        print("entered twoSum: j: ", j)
        print('target: ', target)
        seenNums = set()
        doubles = set()
        for ptr in range(j,len(nums)):
            print("ptr: ", ptr)
            jNum = nums[ptr]
            print("jNum: ", jNum)
            diff = target - jNum
            if diff in seenNums:
                doubles.add((jNum, diff))
            else:
                seenNums.add(jNum)

        return doubles

    # =========================================================

    # Sorted solution
    """
    Time complexity: O(n^2): outer for loop is O(n), inner twoSum is O(n), total O(n^2)
        The sort is O(n log n) but that's eclipsed by the nested for loops.
    Space complexity: O(n): the set seenNums holds about the size of the nums array.
    """

    def threeSum_sorted(self, nums: List[int]) -> List[List[int]]:

        numsSet = set(nums)
        if len(numsSet) == 1 and 0 in numsSet:
            return [[0, 0, 0]]

        nums.sort()
        # print("nums sorted: ", nums)
        triplets = set()
        for i,n in enumerate(nums):
            # print("n: ", n)
            j = i+1
            target = -n
            doubles: List[List] = self.twoSum_sorted(j, nums, target)
            # print("doubles: ", doubles)
            for double in doubles:
                triplet = double
                if n < double[0]:
                    triplet.insert(0, n)
                elif n >= double[0] and n < double[1]:
                    triplet.insert(1, n)
                else:
                    triplet.append(n)
                # print("triplet: ", triplet)
                triplets.add(tuple(triplet))
        tripletsList = [list(tup) for tup in triplets]
        return tripletsList

    def twoSum_sorted(self, j, nums, target):
        seenNums = set()
        doubles = []
        for k in range(j, len(nums)):
            diff = target - nums[k]
            if diff in seenNums:
                if diff > nums[k]:
                    doubles.append([nums[k], diff])
                else:
                    doubles.append([diff, nums[k]])
            else:
                seenNums.add(nums[k])
        return doubles


    # =========================================================

    def validate_triplets(self, answer, expected):
        answerSet = set([tuple(trip) for trip in answer])
        expectedSet = set([tuple(trip) for trip in expected])
        return answerSet == expectedSet

    def test_1(self): 
        test_case = [
            [[-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]],
            # [[0,1,1], []],
            # [[0,0,0], [[0,0,0]]],
            # [[1,2,-2,-1], []],
            # [[3,-2,1,0], []]
        ]

        for tc in test_case:
            nums = tc[0]
            print("test case: ", nums)
            expected = tc[1]
            print("expected: ", expected)
            # output = self.threeSum(nums)
            output = self.threeSum_sorted(nums)
            print("output: ", output)
            validationResult = self.validate_triplets(output, expected)
            print("validationResult: ", validationResult)
            assert validationResult == True


if __name__ == "__main__":
    cl = ThreeSum()
    cl.test_1()