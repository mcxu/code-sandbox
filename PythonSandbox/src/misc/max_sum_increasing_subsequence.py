'''
Max sum increasing subsequence

Given array of integers, return an array of length 2 of the following:
[    Max possible sum given by a subsequence of increasing values,
    [The sequence of increasing values]
]

Sample input: [10, 70, 20, 30, 50, 11, 30]
Sample output: [110, [10, 20, 30, 50]]

https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
https://www.youtube.com/watch?v=99ssGWhLPUE
Related: misc/max_sum_decreasing_subsequece.py, misc/longest_increasing_subsequence.py 
'''

class Prob:
    '''
    n: number of values in array
    Time complexity: O(n^2) since there is a nested for loop going from [0,i] of the outer for loop.
    The while loop to construct the sequence is just O(n).
    Space complexity: O(n) since there are 2 auxiliary arrays to store max sum, and indices, for subproblems.
    '''
    @staticmethod
    def maxSumIncreasingSubsequence(array):
        maxSumUpToVal = [n for n in array]
        
        # at some index i in this array, store the index of the previous array value
        # in the max sum increasing subsequence
        maxSumIndices = [None for n in array]
        maxSumIndex = 0 # index for keeping track of where the index of the max sum is in maxSumUpToVal
        
        for i in range(len(array)):
            print("---")
            print("array: ", array)
            print("maxSumUpToVal before: ", maxSumUpToVal)
            print("maxSumIndices before: ", maxSumIndices)
            inputVal = array[i]
            
            for j in range(0, i):
                upToVal = array[j]
                print("inputVal={}, upToVal={}".format(array[i], upToVal))
                if upToVal < inputVal and inputVal + maxSumUpToVal[j] > maxSumUpToVal[i]:
                    maxSumUpToVal[i] = inputVal + maxSumUpToVal[j]
                    print("    setting maxSumUpToVal[{}] to {}".format(i, inputVal + maxSumUpToVal[j]))
                    maxSumIndices[i] = j
                    print("    setting maxSumIndices[{}] to {}".format(i,j))
                
            if maxSumUpToVal[i] > maxSumUpToVal[maxSumIndex]:
                maxSumIndex = i
                print("maxSumIndex updated: ", maxSumIndex, "    maxSum is now: ", maxSumUpToVal[maxSumIndex])
                        
            print("maxSumUpToVal after: ", maxSumUpToVal)
            print("maxSumIndices after: ", maxSumIndices)
            print("maxSumIndex: ", maxSumIndex)
        
        # construct actual sequence of values    
        maxSumValues = []
        tmpIndex = maxSumIndex
        while tmpIndex != None:
            maxSumValues.insert(0, array[tmpIndex])
            tmpIndex = maxSumIndices[tmpIndex]
        
        print("maxSumValues after: ", maxSumValues)
        print("maxSumIndex after: ", maxSumIndex)
        return [maxSumUpToVal[maxSumIndex], maxSumValues]
                
    @staticmethod
    def test1():
        array = [10, 70, 20, 30, 50, 11, 30]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test1: ans: ", ans)


    @staticmethod
    def test2():
        array = [-1]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test2: ans: ", ans)
        
        
    @staticmethod
    def test3():
        array = [-1, 1] # correct: [1, [1]]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test3: ans: ", ans)
        
    @staticmethod
    def test4():
        array = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50] 
        # correct ans: [164, [10, 11, 14, 23, 25, 31, 50]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test4: ans: ", ans)
        
        
#Prob.test1()
#Prob.test2()
#Prob.test3()
Prob.test4()
