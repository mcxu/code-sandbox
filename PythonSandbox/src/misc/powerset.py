'''
Powerset
Function that takes array of unique integers, and returns powerset.
Powerset of set X, P(X), is set of all subsets of X.

Sample input: [1, 2, 3]
Sample output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
'''

class PS:
    @staticmethod
    def powerset(array):
        pwrset = []
        
        #handle null set
        pwrset.append(set([]))
        
        #handle subsets where 1 < subset.length < len(array)
        # get permutations
        perms = PS.getPermutations(array)
        print("perms: ", perms)
        for count in range(len(array)):
            for perm in perms:
                permset = set(perm[0:count+1])
                print("permset: ", permset)
                
                if permset not in pwrset:
                    pwrset.append(permset)
        
        return [list(subset) for subset in pwrset]
    
    """ Return list of all permutations """
    @staticmethod
    def getPermutations(array):
        return PS.permHelper(array, [])
    
    @staticmethod
    def permHelper(array, perms):
        if array not in perms:
            perms.append(array)
        else:
            return perms
        
        for i in range(len(array)-1):
            arrayCopy = array.copy()
            tmp = arrayCopy[i]
            arrayCopy[i] = arrayCopy[i+1]
            arrayCopy[i+1] = tmp
            PS.permHelper(arrayCopy, perms)
        
        return perms
    
    @staticmethod
    def test1():
        array = [1,2,3]
        ps = PS.powerset(array)
        print("test1: powerset: ", ps)
        
PS.test1()
