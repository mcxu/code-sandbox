"""
Given a collection of distinct integers, return all possible permutations. [Medium]
Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

#import time

class LC46:
    def permute(self, nums):
        # helper function
        def permuteHelper(nums, results):
            if nums in results:
                #print("    list {} already in results.".format(nums))
                return results
            else:
                #print("    appending {} to results.".format(nums))
                results.append(nums)
            #print("results: ", results)
            
            for i in range(len(nums)-1):
                #print("    i:{}, nums:{}".format(i,nums))
                newPerm = nums.copy()
                # swap the ith and (i+1)th, to make a new permutation
                tmp = newPerm[i+1]
                newPerm[i+1] = newPerm[i]
                newPerm[i] = tmp
                #print("    after swap: nums:{}, newPerm:{}".format(nums, newPerm))
                
                # recursive call
                permuteHelper(newPerm, results)
                
            return results
        
        # populate list of results using permuteHelper
        return permuteHelper(nums, [])
            
    def test_permute(self):
        numsList = [
            [1,2,3],
            [1,2,3,4],
            [1,2,3,4,5]
            ]
        for nums in numsList:
            results = self.permute(nums)
            print("test_permute nums: ", nums)
            print("test_permute results: ", results)
            print("test_permute number of permutations: ", len(results))
            print("")
    
def main():
    lc46 = LC46()
    lc46.test_permute()

main()
            
        