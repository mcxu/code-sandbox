class Solution:
    def maxProduct_1pass_simplified(self, nums: [int]) -> int:
        prevMaxUpTo = nums[0]
        prevMinUpTo = nums[0]

        prevMaxPossible = 1
        prevMinPossible = 1 

        currMaxUpTo = nums[0]
        currMinUpTo = nums[0]

        currMaxSoFar = nums[0] # result

        for i in range(1, len(nums)):
            n = nums[i]
            
            prevMaxPossible = max(prevMinUpTo*n, prevMaxUpTo*n)
            currMaxUpTo = max(prevMaxPossible, n)

            prevMinPossible = min(prevMinUpTo*n, prevMaxUpTo*n)
            currMinUpTo = min(prevMinPossible, n)

            if currMaxUpTo > currMaxSoFar:
                currMaxSoFar = currMaxUpTo 

            prevMaxUpTo = currMaxUpTo
            prevMinUpTo = currMinUpTo
        
        return currMaxSoFar


    """ based on Kadanes Algorithm
    Time complexity: O(n) where n ~ len(nums)
    Space complexity: O(1), storage variables do not increase with elements in nums
    """
    def maxProduct_1pass(self, nums: [int]) -> int:
        prevMaxUpTo = nums[0]
        prevMinUpTo = nums[0]

        prevMaxPossible = 1 # intermediate max
        prevMinPossible = 1 # intermediate min

        currMaxUpTo = nums[0]
        currMinUpTo = nums[0]

        currMaxSoFar = nums[0] # result

        for i in range(1, len(nums)):
            n = nums[i]

            # find prevMaxPossible
            if prevMaxUpTo*n > prevMinUpTo*n:
                prevMaxPossible = prevMaxUpTo*n
            else:
                prevMaxPossible = prevMinUpTo*n
            
            # find currMaxUpTo n
            if prevMaxPossible > n:
                currMaxUpTo = prevMaxPossible
            else:
                currMaxUpTo = n

            # find prevMinPossible
            if prevMaxUpTo*n > prevMinUpTo*n:
                prevMinPossible = prevMinUpTo*n
            else:
                prevMinPossible = prevMaxUpTo*n
            
            # update currMinUpTo n
            if prevMinPossible > n:
                currMinUpTo = n
            else:
                currMinUpTo = prevMinPossible

            # update maxSoFar
            if currMaxUpTo > currMaxSoFar:
                currMaxSoFar = currMaxUpTo

            # set the current values to previous for the next iteration
            prevMaxUpTo = currMaxUpTo
            prevMinUpTo = currMinUpTo

        return currMaxSoFar


    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def maxProduct_2pass(self, nums: [int]) -> int:
        if not nums:
            return 0

        maxProdUpTo = nums[0]

        runningProd = 1
        for i in range(len(nums)):
            runningProd *= nums[i]
            maxProdUpTo = max(maxProdUpTo, runningProd)

            if runningProd == 0:
                runningProd = 1

        runningProd = 1
        for i in range(len(nums)-1, -1, -1):
            runningProd *= nums[i]
            maxProdUpTo = max(maxProdUpTo, runningProd)

            if runningProd == 0:
                runningProd = 1
        
        return maxProdUpTo

    def test(self):
        cases = [
            dict(nums=[2,3,-2,4], output=6),
            # dict(nums=[-2,0,-1], output=0)
            # dict(nums=[0,2], output=2)
            # dict(nums=[-2], output=-2)
        ]

        for c in cases:
            # res = self.maxProduct_2pass(c["nums"])
            res = self.maxProduct_1pass_simplified(c["nums"])
            print("case: ", c["nums"])
            print("res: ", res)
            assert res == c["output"]



sol = Solution()
sol.test()