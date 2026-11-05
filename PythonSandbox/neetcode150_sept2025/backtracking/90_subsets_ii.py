class Solution:
    """ Let n = len(nums)
    TC: O(n * 2^n * n * logn) = O(n * 2^n * logn)
        Outer for loop iterates n times, inner for loop makes powerset grow 2x each time it runs fully, 
        which then makes it run 2x iterations from there, and so on.
        Sort operation is closer to O(log n), not the upper bound of O(n log n) 
        since the sorting is done on subsets rather than the whole list of nums.
    SC: O(n * 2^n)
        powerset: O(n * 2^n), powerset gets added to by iterations that following the time complexity, but leave the sort out since that is done in place.
        seensubsets: same as powerset 
    """
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        powerset = [[]]
        seensubsets = set[tuple]()
        for i in range(len(nums)):
            for j in range(len(powerset)):
                print("------ j=", j)
                subset = powerset[j] + [nums[i]]
                subset.sort()
                #print("subset: ", subset)
                subsetTup = tuple(subset)
                print("subsetTup: ", subset)
                if subsetTup not in seensubsets:
                    powerset.append(subset)
                seensubsets.add(subsetTup)

        return powerset
    
    def test1(self):
        nums = [1,2,2]
        expected = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        result = self.subsetsWithDup(nums)
        print("result:\n", result)
        assert set(tuple(r) for r in result) == set(tuple(r) for r in expected)
        
    def test4(self):
        nums = [4,4,4,1,4]
        expected = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
        result = self.subsetsWithDup(nums)
        print("result:\n", result)
        assert set(tuple(r) for r in result) == set(tuple(r) for r in expected)

if __name__ == "__main__":
    s = Solution()
    # s.test1()
    s.test4()
