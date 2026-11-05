from typing import List

class Solution:
    """ Let n = len(nums)
    TC: O(n * 2^n), outer for loop iterates n times, inner for loop makes each starting powerset that the loop begins with grow 2x, 
        which then iterates from there on the next time the program gets to the inner for loop, and so on.
    SC: Same as time complexity.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for i in range(len(nums)):
            for j in range(len(powerset)):
                subset = powerset[j] + [nums[i]]
                powerset.append(subset)
        # print("powerset: ", powerset)
        return powerset
    
    def test1(self):
        nums = [1,2,3]
        result = self.subsets(nums)
        print("result: ", result)

if __name__ == "__main__":
    s = Solution()
    s.test1()