'''
Kadane's Algorithm (max sum subarray)
Given input array of integers, return max sum from the subarray 
that consists only of adjacent values from the input array.

Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])
'''

class KD:
    
    """
    Algorithm: maxEndingHere = max{maxEndingHere + array[i], array[i]}
    Time complexity: O(n), where n=num elements in array. Since this is a single pass through array.
    Space complexity: O(1), since maxSoFar and maxEndingHere just stores the latest maxes (single value).
    """
    @staticmethod
    def kadanesAlgorithm(array):
        maxEndingHere = array[0]
        maxSoFar = maxEndingHere
        for i in range(1, len(array)):
            val = array[i]
            maxEndingHere = max(val, maxEndingHere+val)
            print("maxEndingHere: ", maxEndingHere)
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
        return maxSoFar
            
    '''
    Version of kadanes that also gives the actual subarray, using variables that keep track of 
    latest starting subarray index and max so far index.
    '''
    @staticmethod
    def kadanesWithSubarray(array):
        #maxEndingHere = array[0]
        maxEndingHere = array[0]
        maxSoFar = array[0]
        maxSoFarInd = 0
        mssStartInd = 0 # max sum subarray start index: the index of the latest value where array value == maxEndingHere
        
        for i in range(1, len(array)):
            val = array[i]
            if maxEndingHere + val > val:
                maxEndingHere = maxEndingHere + val
            else:
                maxEndingHere = val
                mssStartInd = i
            
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
                maxSoFarInd = i
        
        print("maxEndingHere: ", maxEndingHere)
        print("maxSoFar: ", maxSoFar)
        print("mssStartInd: ", mssStartInd)
        print("maxSoFarInd: ", maxSoFarInd)
        
        return [maxSoFar, array[mssStartInd:maxSoFarInd+1]]
    
    """
    Brute force:
    Time complexity: O(n^2), where n=len(array)
    Space complexity: O(1), because maxSum only stores the highest sum so far
    """
    @staticmethod
    def maxSumSubArrayBruteForce(array):
        maxSum = -float("inf")
        for i in range(len(array)):
            val = array[i]
            print("i= %s, val= %s" % (i ,val))
            
            for j in range(i+1, len(array)+1):
                print("    j=", j)
                subarray = array[i:j]
                print("        subarray: ", subarray)
                saSum = sum(subarray)
                print("        saSum: ", saSum)
                if saSum > maxSum:
                    maxSum = saSum
                    print("        maxSum set to: ", maxSum)
        return maxSum
                
    
    @staticmethod
    def test1(alg):
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        #ans: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])
        ans = alg(array)
        print("test1 ans: ", ans)
    
    @staticmethod
    def test2(alg):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #ans: 55
        ans = alg(array)
        print("test2 ans: ", ans)
    
    @staticmethod
    def test3(alg):
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] #ans: -1
        ans = alg(array)
        print("test3 ans: ", ans)
   

alg  = KD.kadanesAlgorithm
#alg = KD.kadanesWithSubarray 
KD.test1(alg)
#KD.test2() 
#KD.test3()      

    
