'''
Longest Increasing Subsequence

Given array of ints, find the longest subsequence that has all values in increasing order.
Also return the values themselves.

Examples:
Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}

https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
'''

class Prob:
    '''
    n: number of values in array
    Time complexity: O(n^2), since there is a nested for loop going from [0,i] of the outer for loop.
    Space complexity: O(n) since longestUpToVal stores at most n elements.
    '''
    @staticmethod
    def longestIncreasingSubsequence(array):
        # stores the length of the longest increasing subsequence up to a val corresponding to index.
        # Init to all 1 because the longest increasing subsequence of a val by itself is 1.
        longestUpToVal = [1 for _ in array] 
        
        #store the index of the previous number in the longest increasing subsequence
        longestIncIndices = [None for _ in array] 
        
        # store the index of the longest increasing subsequence count so far
        longestSeqInd = 0
        
        for i in range(len(array)):
            iVal = array[i]
            
            for j in range(0, i):
                jVal = array[j]
                
                if jVal < iVal and longestUpToVal[j]+1 > longestUpToVal[i]:
                    longestUpToVal[i] = longestUpToVal[j]+1
                    print("longestUpToVal: ", longestUpToVal)
                    longestIncIndices[i] = j
                    print("longestIncIndices: ", longestIncIndices)
            
            if longestUpToVal[i] > longestUpToVal[longestSeqInd]:
                longestSeqInd = i
                print("longestSeqInd: ", longestSeqInd)
            
        longestSubseq = []
        tmpIndex = longestSeqInd
        while tmpIndex != None:
            longestSubseq.insert(0, array[tmpIndex])
            tmpIndex = longestIncIndices[tmpIndex]
        print("longestSubseq: ", longestSubseq)
        return [max(longestUpToVal), longestSubseq]
    
    @staticmethod
    def test1():
        array = [3, 10, 2, 1, 20]
        #array = [3,2]
        #array = [50, 3, 10, 7, 40, 80]
        #array = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        ans = Prob.longestIncreasingSubsequence(array)
        print("ans: ", ans)
        
Prob.test1()
                