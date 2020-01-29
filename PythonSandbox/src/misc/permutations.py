'''
Function that takes an array of unique ints and returns array of all permutations.
If input array is empty, return empty array.
Sample input: [1, 2, 3]
Sample output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''
import time

class Prob:
    @staticmethod
    def getPermutations(array):
        if not array:
            return array
        return Prob.permHelper(array, [])
    
    @staticmethod
    def permHelper(array, perms):
        print("*** array: {}, perms: {}".format(array, perms))
        if array not in perms:
            perms.append(array.copy())
            print("    added to perms: ", perms)
        else:
            print("    terminating with array: ", array)
            return perms
        
        for i in range(0, len(array)-1):
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp
            
            arrayCopy = array.copy()
            print("    arrayCopy: {}, arrayCopy addr: {}".format(arrayCopy, id(arrayCopy)))
            Prob.permHelper(arrayCopy, perms)
        
        return perms
    
    @staticmethod
    def test1():
        array = [1, 2, 3]
        correctResult = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        res = Prob.getPermutations(array)
        eq = (len(res) == len(correctResult)) and all(perm in correctResult for perm in res)
        print("test1: eq: ", eq)

Prob.test1()