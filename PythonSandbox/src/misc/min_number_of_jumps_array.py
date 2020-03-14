'''
Minimum number of jumps in an array

Given an array of ints, each int represents the max number of jumps forward from the int's index. 
Write function to figure out the miniumum number of jumps to get from the 0th index to the final index.

Sample input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
Sample output: 4
    (3 --> 4 --> 3 --> 7 --> 3)
    (3 --> 2 --> 2 --> 7 --> 3)
'''

class Prob:
    '''
    Brute force recursive solution. Forms a tree of jumps. For example (parenthesis nums are indices): 
    3->{4(1), 2(2) , 1(3)}
    4->{2(2), 1(3), 2(4), 3(5)}, 2->{1(3), 2(4)}, 1->{2(4)} and so on.
    '''
    @staticmethod
    def minNumberOfJumps(array):
        # jumpCounter() counts the running total of jumps in the "tree" of jumps, recursively.
        # the nonlocal minJumps gets updated if current index >= end index, thus updating minJumps for a path in the tree.
        def jumpCounter(array, ind, jumpsInPath):
            nonlocal minJumps
            print("ind: {}, jumpsInPath: {}, minJumps: {}".format(ind, jumpsInPath, minJumps))
            if ind >= len(array)-1:
                print("    end condition reached")
                if jumpsInPath < minJumps:
                    minJumps = jumpsInPath
                    print("    updated minJumps: ", minJumps)
                return 
            
            # recursive call for immediate children (children means numbers that current number can jump to)
            for i in range(1, array[ind]+1):
                jumpCounter(array, ind+i, jumpsInPath+1)
        
        minJumps = float('inf') # assume the largest number possible of jumps initially
        jumpsInPath = 0
        ind = 0 # starting index
        jumpCounter(array, ind, jumpsInPath)
        return minJumps
    
    '''
    Dynamic programming solution
    '''
    @staticmethod
    def minNumberOfJumpsDP(array):
        pass
    
    @staticmethod
    def test1(alg):
        array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
        res = alg(array)
        print("test1 res: ", res)

    @staticmethod
    def test2(alg):
        array = [1 for _ in range(10)]
        array[5] = 10
        print("test2 array: ", array)
        res = alg(array)
        print("test2 res: ", res)
    
def main():
    alg1 = Prob.minNumberOfJumps
    alg2 = Prob.minNumberOfJumpsDP
    
    Prob.test1(alg2)
    #Prob.test2(alg1)
    
main()
