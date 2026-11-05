class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = set[tuple]()
        self.permuteHelper(nums, results)
        resultsList = [list(r) for r in results]
        return resultsList

    def permuteHelper(self, nums, results:set) -> set(tuple):
        numsTup = tuple(nums)
        if numsTup in results:
            return
        else:
            results.add(numsTup)
        
        for i in range(len(nums)-1):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            self.permuteHelper(nums, results)
            nums[i], nums[i+1] = nums[i+1], nums[i]
        
        return 

    def test1(self):
        nums = [1,2,3]
        perms = sorted(self.permute(nums))
        print("perms:\n", perms)
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        assert perms == expected

if __name__ == "__main__":
    s = Solution()
    s.test1()