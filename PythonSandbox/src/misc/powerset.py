'''
Powerset
Function that takes array of unique integers, and returns powerset.
Powerset of set X, P(X), is set of all subsets of X.

Sample input: [1, 2, 3]
Sample output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
'''

class PS:
    
    """
    Time complexity:
        O(n!*n): get permutations
        O(n*n!): nested for loop
        O(2^n): turn each subset into list, done once at end
        Total: 2*O(n!*n) + O(2^n) = O(n!*n)
    Space complexity:
        O(n!*n): get permutations
        O(2^n): number of subsets
        Total: O(n!*n) + O(2^n) = O(n!*n)
    """
    @staticmethod
    def powerset(array):
        pwrset = [] # space: O(2^n) subsets for a set of n values
        
        #handle null set
        pwrset.append(set([]))
        
        #handle subsets where 1 < subset.length < len(array)
        # get permutations
        perms = PS.getPermutations(array) # Time: O(n!*n), Space: O(n!*n)
        print("perms: ", perms)
        for count in range(len(array)): # time: O(n)
            for perm in perms: # time: O(n!)
                permset = set(perm[0:count+1])
                print("permset: ", permset)
                
                if permset not in pwrset:
                    pwrset.append(permset) # space: O(2^n) subsets
        
        return [list(subset) for subset in pwrset] # time: O(2^n) once
    
    """ Return list of all permutations """
    @staticmethod
    def getPermutations(array):
        return PS.permHelper(array, [])
    
    @staticmethod
    def permHelper(array, perms):
        if array not in perms:
            perms.append(array.copy())
        else:
            return perms
        
        for i in range(len(array)-1):
            array[i], array[i+1] = array[i+1], array[i]
            PS.permHelper(array, perms)
            array[i], array[i+1] = array[i+1], array[i]
        
        return perms


    @staticmethod
    def test1():
        array = [1,2,3]
        ps = PS.powerset(array)
        print("test1: powerset: ", ps)

    """
    Time complexity: O(n * 2^n)
    Space complexity: There are 2^n subsets, each subset has on average len(n)/2 elements. O(n * 2^n)
    """
    @staticmethod
    def powersetIterative(array):
        pwrset = [[]] # pre append the empty set
        for val in array: # time O(n)
            print("== val: ", val)
            for i in range(len(pwrset)): # time O(2^n) b/c at the final iteration of powerset for each val, there are twice as many subsets as previously
                print("i: ", i)
                currentSubset = pwrset[i]
                print("currentSubset: ", currentSubset)
                pwrset.append(currentSubset + [val])
                print("pwrset after append: ", pwrset)
        
        return pwrset
                  
    @staticmethod
    def test2():
        array = [1,2,3,4]
        ps = PS.powersetIterative(array)
        print("test2: powerset: ", ps)
                   
#PS.test1()
PS.test2()

