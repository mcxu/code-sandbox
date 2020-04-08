'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the 
sum of elements in both subsets is equal.
'''

class Solution:
    '''
    Let n = len(nums)
    Time complexity: O(2^n), each call of helper results in 2 recursive helper calls.
    Space complexity: O(n), since there are at most n helper calls on the call stack.
    '''
    def canPartition(self, nums):
        numSum = sum(nums) # O(n) time
        print("numSum: ", numSum)
        if numSum % 2 == 0:
            print("calling helper")
            targetSum = numSum/2
            return self.helper(nums, len(nums)-1, targetSum)
        
        return False
    
    def helper(self, nums, i, targetSum):
        if targetSum == 0:
            return True
        if targetSum < 0:
            return False
        if i < 0:
            return False
        
        excludeVal = self.helper(nums, i-1, targetSum)
        includeVal = self.helper(nums, i-1, targetSum-nums[i])
        return excludeVal | includeVal
    
    #-----------------------------------------------------------
    
    '''
    Let n = len(nums)
    Time complexity: O(n). 
        Each call of helper results in 2 calls of helper. 
        However 1 of those calls is memoized O(1),
        so the order is O(2*n*1), which is O(n).
    Space complexity: O(n)
        At most n calls on the recursive call stack. O(n). There are n items memoized. O(n)
        So the total is O(2n), which is O(n).
    '''
    def canPartitionMemo(self, nums):
        numSum = sum(nums)
        
        if numSum % 2 == 0:
            targetSum = numSum/2
            memo = {}
            return self.helperMemo(nums, len(nums)-1, targetSum, memo)
        
        return False
    
    def helperMemo(self, nums, i , targetSum, memo):
        if targetSum == 0:
            return True
        if targetSum < 0:
            return False
        if i < 0:
            return False
        
        if targetSum in memo.keys():
            return memo[targetSum]
        
        excludeVal = self.helperMemo(nums, i-1, targetSum, memo)
        includeVal = self.helperMemo(nums, i-1, targetSum-nums[i], memo)
        memo[targetSum] = (excludeVal | includeVal)
        return memo[targetSum]
    
    def test1(self, alg):
        nums = [1, 5, 11, 5] 
        #Output: true
        #Explanation: The array can be partitioned as [1, 5, 5] and [11].
        res = alg(nums)
        print("test1 res: ", res)
    
    def test2(self, alg):
        nums = [1, 2, 3, 5]
        #Output: false
        #Explanation: The array cannot be partitioned into equal sum subsets.
        res = alg(nums)
        print("test1 res: ", res)

s = Solution()
#alg = s.canPartition
alg = s.canPartitionMemo
s.test1(alg)
#s.test2(alg)