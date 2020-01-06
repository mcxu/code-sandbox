'''
Kadane's Algorithm
Given input array of integers, return max sum from the subarray 
that consists only of adjacent values from the input array.

Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])
'''

class KD:
    
    # TODO: Not completely correct. Need to fix.
    @staticmethod
    def kadanesAlgorithm(array):
        # array for storing sum from ith value
        sums = [0 for i in range(len(array))]
        print("sums init: ", sums)
        
        maxSub = sums
        for i in range(len(array)):
            val = array[i]
            print("i= %s, val= %s" % (i ,val))
            print("    rest of array: ", array[i:])
            print("    sum: ", sum(array[i:]))
            
            if sum(array[i:]) > max(sums):
                maxSub = array[i:]
                print("    maxSub updated to: ", maxSub)
            
            sums[i] = sum(array[i:])
            print("    sums: ", sums)
            
        print("sums after: ", sums)
        print("maxSub: ", maxSub)
        maxSum = max(sums)
        for i in range(len(maxSub), -1, -1):
            print("i = ", i)
            print("    maxSub: ", maxSub[0:i])
            print("    sum of maxSub: ", sum(maxSub[0:i]))
            if sum(maxSub[0:i]) > max(sums):
                maxSum = sum(maxSub[0:i])
                print("    maxSum updated to: ", maxSum)
        
        print("maxSum: ", maxSum)
        return maxSum
                
    
    @staticmethod
    def test1():
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        KD.kadanesAlgorithm(array)
    
    @staticmethod
    def test2():
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #ans: 55
        KD.kadanesAlgorithm(array)
    
    @staticmethod
    def test3():
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] #ans: -1
        KD.kadanesAlgorithm(array)
        
#KD.test1()
#KD.test2() 
KD.test3()      

    
