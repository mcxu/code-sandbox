"""
Function that takes non-empty array of distinct integers,
and an target sum integer. Find all triplets in the array that
sum up to the target sum and return 2-d array of these triplets.
Numbers in each triplet must be in ascending order, and the triplets
themselves must be in ascending order according to the numbers they hold.

input: ([12, 3, 1, 2, -6, 5, -8, 6], 0)
output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

class TNS:
    
    @staticmethod
    def threeNumberSum(array, targetSum):
        validTriplets = []
        
        return validTriplets
    
    @staticmethod
    def test_threeNumberSum():
        #l = [12, 3, 1, 2, -6, 5, -8, 6]
        l = [12, 3, 1, 2, -6, 5, -8, 6]
        ts = 0
        output = TNS.threeNumberSum(l, ts)
        print("output: ", output)


def main():
    #ThreeNumSum.test_threeNumberSum()
    pass
    
main()


"""
http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
https://stackoverflow.com/questions/49248668/combinations-sum-depth-first-search-solution
"""