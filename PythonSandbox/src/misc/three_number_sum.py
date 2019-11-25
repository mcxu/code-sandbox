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
    
    """
    find all combinations (order doesn't matter) of size k in array using depth first search
    returns combination lists in sorted order, and values of each list is also sorted.
    """
    @staticmethod
    def arrayCk(inputArray, k):
        
        #uses DFS to traverse all combinations of size k 
        def dfsHelper(inputArray, k, visited=[], solns=[]):
            num = inputArray.pop(0)
            print("num: ", num)
            visited.append(num)
            print("    visited:", visited)
            for num in visited:
                print("    inputArray:", inputArray)
                
                combo = [visited[0]]
                combo.append(inputArray[0])
                print("    combo:", combo)
                
                solns.append(combo)
                print("    solns:",solns)
                
                dfsHelper(inputArray, k, visited, solns)
            return visited
        
        return dfsHelper(inputArray, k, [])
                  
    @staticmethod
    def test_arrayCk():
        l = [1,2,3,4,5]
        result = TNS.arrayCk(l, 3)
        print("test_arrayCk: result: ", result)


    # https://stackoverflow.com/questions/12970897/can-you-explain-this-recursive-n-choose-k-code-to-me  
    # n Combination k (finds number of combos, but not the combos themselves)
    @staticmethod
    def nCk(n, k): 
        if k == 0:
            return 1
        if n == k:
            return 1
        else:
            return TNS.nCk(n-1, k-1) + TNS.nCk(n-1, k)
    
    @staticmethod
    def test_nCk():
        numsList = [
            [1,2,3,4],
            [12, 3, 1, 2, -6, 5, -8, 6]
            ]
        for nums in numsList:
            results = TNS.nCk(len(nums), 3)
            print("test_subset: input: ", nums)
            print("test_subset: number of permutations: ", results)
            print("")


def main():
    #ThreeNumSum.test_threeNumberSum()
    #TNS.test_nCk()
    TNS.test_arrayCk()
    pass
    
main()


"""
http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
https://stackoverflow.com/questions/49248668/combinations-sum-depth-first-search-solution
"""