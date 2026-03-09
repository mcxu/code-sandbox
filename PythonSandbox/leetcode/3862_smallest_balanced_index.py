class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        print("nums: ", nums)
        if not nums:
            return -1

        sumsFromLeft = [0]
        for i in range(len(nums)):
            sumsFromLeft.append(sumsFromLeft[-1] + nums[i])
        print("sumsFromLeft: ", sumsFromLeft)
        
        prodFromRight = 1
        for i in range(len(nums)-1, -1, -1):
            # print("i: ", i, "prodFromRight: ", prodFromRight, "sumsFromLeft[i]: ", sumsFromLeft[i])
            if sumsFromLeft[i] == prodFromRight:
                return i
            prodFromRight *= nums[i]
        
        return -1

    def test1(self):
        nums = [2, 1, 2]
        result = self.smallestBalancedIndex(nums)
        print("result: ", result)
        assert result == 1

    def test2(self):
        nums = [2,8,2,2,5]
        result = self.smallestBalancedIndex(nums)
        print("result: ", result)
        assert result == 2
    
    def test3(self): 
        nums = [1]
        result = self.smallestBalancedIndex(nums)
        print("result: ", result)
        assert result == -1

    def test4(self):
        nums = [1, 2, 3, 4, 5]
        result = self.smallestBalancedIndex(nums)
        print("result: ", result)
        assert result == -1

    def test5(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.smallestBalancedIndex(nums)
        print("result: ", result)
        assert result == -1
    
    def test6(self):
        nums = [1,3]
        result = self.smallestBalancedIndex(nums)
        print("result: ", result)
        assert result == 1

if __name__ == "__main__":
    s = Solution()
    s.test1()
    s.test2()
    s.test3()
    s.test4()
    s.test5()
    s.test6()
