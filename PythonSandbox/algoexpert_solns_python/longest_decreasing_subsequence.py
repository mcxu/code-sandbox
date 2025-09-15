'''
Longest decreasing subsequence

Given array of ints, find the longest subsequence that has all values in increasing order.
Also return the values themselves.

Examples:
Input: arr[] = [15, 27, 14, 38, 63, 55, 46, 65, 85]
Output: 3
Explanation: The longest decreasing sub sequence is [63, 55, 46]

Input: arr[] = [50, 3, 10, 7, 40, 80]
Output: 3
Explanation: The longest decreasing subsequence is [50, 10, 7]

https://www.geeksforgeeks.org/longest-decreasing-subsequence/
'''

class Prob:
    @staticmethod
    def longestDecreasingSubsequence(array):
        # store longest decreasing subsequence up to a val in the input array.
        longestUpToVal = [1 for _ in array]
        
        # store index of the previous number in longest decreasing subsequence.
        longestDecIndices = [None for _ in array]
        
        # store the index of the longest decreasing subsequence count so far
        longestSeqInd = 0
        
        for i in range(len(array)):
            inputVal = array[i]
            
            for j in range(0,i):
                upToVal = array[j]
                
                if upToVal > inputVal and longestUpToVal[j]+1 > longestUpToVal[i]:
                    longestUpToVal[i] = longestUpToVal[j]+1
                    longestDecIndices[i] = j
                print("longestUpToVal: ", longestUpToVal)
            
            if longestUpToVal[i] > longestUpToVal[longestSeqInd]:
                longestSeqInd = i
        
        longestSubseq = []
        tmpInd = longestSeqInd
        while tmpInd != None:
            longestSubseq.insert(0, array[tmpInd])
            tmpInd = longestDecIndices[tmpInd]
            
        return [max(longestUpToVal), longestSubseq]
    
    @staticmethod
    def test1():
        #array = [50, 3, 10, 7, 40, 80]
        array = [15, 27, 14, 38, 63, 55, 46, 65, 85]
        ans = Prob.longestDecreasingSubsequence(array)
        print("test1: ans: ", ans)

Prob.test1()
