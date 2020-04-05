'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, find the total number of 
continuous subarrays whose sum equals to k.
'''

class Solution:
    '''
    Brute force solution.
    '''
    def subarraySum(self, nums, k):
        count = 0
        jterm = 0
        while jterm < len(nums): 
            i = 0
            j = jterm
            ijsum = sum(nums[i:j+1])
            if ijsum == k:
                count += 1
            i += 1
            j += 1
            while j < len(nums):
                ijsum = ijsum - nums[i-1] + nums[j]
                if ijsum == k:
                    count += 1
                i += 1
                j += 1
            
            jterm += 1
        
        return count
    
    '''
    Using map to store mapping:
    running sum : number of times that running sum occurs from 0 to that running sum.
    
    Idea: diff of runsum(num[0:i]) - runsum(num[0:j]) = k, (where j <= i)
    So runsum(num[0:j]) = runsum(num[0:i])-k
    So mathematically: freq[runsum(num[0:j])] = freq[runsum(num[0:i])-k]
    Then:   count += freq[runsum(num[0:j])], which is the same as
            count += freq[runsum(num[0:i])-k]
    '''
    def subarraySum2(self, nums, k):
        count = 0
        runSum = 0
        sumMap = {}
        sumMap[0] = 1 # for the case that runSum-k exists, and is = 0.
        for i in range(len(nums)):
            runSum += nums[i]
            if runSum-k in sumMap.keys():
                count += sumMap[runSum-k]

            if runSum in sumMap.keys():
                sumMap[runSum] = sumMap[runSum]+1
            else:
                sumMap[runSum] = 1
        
        print("sumMap: ")
        for key in sumMap.keys():
            print("    {} : {}".format(key, sumMap[key]))
        return count
    
    def test1(self,alg):
        nums = [1,1,1]
        k = 2
        
#         nums = [1,2,3]
#         k = 3
        c = alg(nums, k)
        print("test1 c: ", c)
    
    def test2(self, alg):
        nums = [1,2,3,4,5,0]
        k = 9
        # expected = 3
        c = alg(nums, k)
        print("test2 c: ", c)
    
    def test3(self, alg):
        nums = [1,2,1,2,1]
        k = 3
        # expected = 4
        c = alg(nums, k)
        print("test3 c: ", c)
        
sol = Solution()
sol.test1(sol.subarraySum2)
#sol.test2(sol.subarraySum2)
#sol.test3(sol.subarraySum2)