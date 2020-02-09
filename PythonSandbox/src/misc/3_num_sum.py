"""
Function that takes non-empty array of distinct integers,
and an target sum integer. Find all triplets in the array that
sum up to the target sum and return 2-d array of these triplets.
Numbers in each triplet must be in ascending order, and the triplets
themselves must be in ascending order according to the numbers they hold.

input: ([12, 3, 1, 2, -6, 5, -8, 6], 0)
output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

import sys
sys.setrecursionlimit(10**6)

class TNS:
    
    @staticmethod
    def threeNumberSum(array, targetSum):
        validTriplets = []
        arrSorted = sorted(array)
        for i in range(len(arrSorted)-1):
            arr = arrSorted[i:]
            print("i= ", i)
            print("arr: ",arr)
            TNS.helper(arr, targetSum, validTriplets, 0, 1, len(arr)-1)
        return validTriplets
    
    
    #p1: pointer to 1st index,  p2: ptr to 2nd index, p3: ptr to 3rd index.
    @staticmethod
    def helper(array, targetSum, validTriplets, i1, i2, i3):
        print("helper: i1={}, i2={}, i3={}".format(i1,i2,i3))
        n1 = array[i1]; n2 = array[i2]; n3 = array[i3]
        sum = n1 + n2 + n3
        
        if i2 == i3:
            return
        
        if sum == targetSum:
            validTriplets.append([n1,n2,n3])
        
        if sum > targetSum:
            TNS.helper(array, targetSum, validTriplets, i1, i2, i3-1)
        else:
            TNS.helper(array, targetSum, validTriplets, i1, i2+1, i3)
         
    
    @staticmethod
    def test_threeNumberSum():
        #l = [12, 3, 1, 2, -6, 5, -8, 6]
        l = [12, 3, 1, 2, -6, 5, -8, 6]
        ts = 0
        output = TNS.threeNumberSum(l, ts)
        print("output: ", output)
        
    

def main():
    TNS.test_threeNumberSum()
    pass
    
main()


"""
http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
https://stackoverflow.com/questions/49248668/combinations-sum-depth-first-search-solution
"""