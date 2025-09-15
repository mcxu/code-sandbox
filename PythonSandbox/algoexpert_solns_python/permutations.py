'''
Function that takes an array of unique ints and returns array of all permutations.
If input array is empty, return empty array.
Sample input: [1, 2, 3]
Sample output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''
import sys

class Prob:
    @staticmethod
    def getPermutations(array):
        if not array:
            return array
        return Prob.permHelper(array, [])
    
    """
    Recursive tree for [1,2,3]. (T) means terminate recursion because perm is already found:
                  ______  1,2,3  ______
                 /                     \
             2,1,3                     1,3,2
            /    \                   /      \
    1,2,3(T)     2,3,1             3,1,2     1,2,3(T)
                /    \            /     \
            3,2,1    2,1,3(T)   1,3,2(T) 3,2,1(T)
           /     \
    2,3,1(T)    3,1,2(T)
    
    Time complexity: 
        n! permutations (n! appends to perms array), 
        n calls to helper method, 
        array.copy() is a O(n) operation but the copy is only done once at the nth call for some given array, 
        the swaps are O(1)
        Therefore, time complexity is O(n! * n +  1 * n + 1), or O(n!*n)
    Space complexity:
        n! permutations, each permutation has length n
        Therefore, space complexity is O(n! * n)
    """
    @staticmethod
    def permHelper(array, perms):
        print("== array: {}, perms: {}".format(array, perms))
        if array not in perms:
            perms.append(array.copy()) # copy is O(n) operation
            #print("    added to perms: ", perms)
        else:
            #print("    terminating with array: ", array)
            return perms
        
        for i in range(0, len(array)-1):
            array[i], array[i+1] = array[i+1], array[i] # swap
            
            print("    array: {}, array addr: {}".format(array, id(array)))
            Prob.permHelper(array, perms) # n calls of helper function
            
            array[i], array[i+1] = array[i+1], array[i] # swap back
        
        return perms
    
    @staticmethod
    def test1():
        array = [1, 2, 3]
        correctResult = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        res = Prob.getPermutations(array)
        print("num of perms: ", len(res))
        eq = (len(res) == len(correctResult)) and all(perm in correctResult for perm in res)
        print("test1: eq: ", eq)


limBefore = sys.getrecursionlimit()
print("limBefore: ", limBefore)
sys.setrecursionlimit(100000)
limAfter = sys.getrecursionlimit()
print("limAfter: ", limAfter)

Prob.test1()