'''
Kadane's Algorithm
Given input array of integers, return max sum from the subarray 
that consists only of adjacent values from the input array.

Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])
'''

class KD:
    
#     @staticmethod
#     def kadanesAlgorithm(array):
#         pass
    
    
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
    def test1():
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] #ans: 19
        ans = KD.kadanesAlgorithm(array)
        print("test1 ans: ", ans)
    
    @staticmethod
    def test2():
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #ans: 55
        ans = KD.kadanesAlgorithm(array)
        print("test2 ans: ", ans)
    
    @staticmethod
    def test3():
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] #ans: -1
        ans = KD.kadanesAlgorithm(array)
        print("test3 ans: ", ans)
        
#KD.test1()
#KD.test2() 
#KD.test3()      

    
