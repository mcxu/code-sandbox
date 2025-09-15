'''
Max sum decreasing subsequence

Given array of ints, return the max sum that can be summed from a decreasing subsequence,
and also return the sequence itself. Return Format: [maxSum, [sequence]]

https://www.geeksforgeeks.org/maximum-sum-decreasing-subsequence/
Related: misc/max_sum_increasing_subsequece.py, misc/longest_decreasing_subsequence.py 
'''

class Prob:
    @staticmethod
    def maxSumDecreasingSubsequence(array):
        # stores the max sum for some value in the array, at the corresponding index.
        # starts with the array itself, because the max sum of any single number is itself.
        maxSumUpToVal = array.copy()
        
        # stores the index (referencing input array) of the previous array value 
        # in the max sum decreasing subsequence. Init to None's because this is
        # used to iterate through the sequence indices in array and get their values
        # until None is reached.
        maxSumIndices = [None for _ in array]
        
        # store index of the max sum found in maxSumUpToVal
        maxSumInd = 0
        
        for i in range(len(array)):
            inputVal = array[i]
            
            for j in range(0, i):
                upToVal = array[j]
                
                # 1st cond: make sure that stopVal is less than upToVal to maintain decreasing order
                # 2nd cond: for the upToVal's index in maxSumUpToVal, ensure that adding the jth val
                # in maxSumUpToVal to upToVal is greater than what is already in maxSumUpToVal[i].
                if upToVal > inputVal and maxSumUpToVal[j] + inputVal > maxSumUpToVal[i]:
                    maxSumUpToVal[i] = maxSumUpToVal[j] + inputVal
                    maxSumIndices[i] = j # index of previous val in max sum dec subsequence
                    
            # update max sum index in maxSumUpToVal
            if maxSumUpToVal[i] > maxSumUpToVal[maxSumInd]:
                maxSumInd = i
                
        # generate sequence
        print("generate seq from maxSumIndices: ", maxSumIndices)
        print("maxsumInd: ", maxSumInd)
        maxSumDecSubseq = []
        tmpInd = maxSumInd
        while tmpInd != None:
            maxSumDecSubseq.insert(0, array[tmpInd])
            print("maxSumDecSubseq: ", maxSumDecSubseq)
            tmpInd = maxSumIndices[tmpInd]
        
        return [max(maxSumUpToVal), maxSumDecSubseq]
    
    
    @staticmethod
    def test1():
        array = [50, 3, 10, 7, 40, 80]
        result = Prob.maxSumDecreasingSubsequence(array)
        print("test1 result: ", result)

Prob.test1()