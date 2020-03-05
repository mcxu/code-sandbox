'''
https://www.geeksforgeeks.org/longest-decreasing-subsequence/

Examples:
Input: arr[] = [15, 27, 14, 38, 63, 55, 46, 65, 85]
Output: 3
Explanation: The longest decreasing sub sequence is [63, 55, 46]

Input: arr[] = [50, 3, 10, 7, 40, 80]
Output: 3
Explanation: The longest decreasing subsequence is [50, 10, 7]
'''

class Prob:
    @staticmethod
    def longestDecreasingSubsequence(array):
        # store longest decreasing subsequence up to a val in the input array.
        longestUpToVal = [1 for _ in array]
        
        for i in range(len(array)):
            inputVal = array[i]
            
            for j in range(0,i):
                upToVal = array[j]
                
                if upToVal > inputVal:
                    longestUpToVal[i] = max(longestUpToVal[j]+1, longestUpToVal[i])
                print("longestUpToVal: ", longestUpToVal)
        return max(longestUpToVal)
    
    @staticmethod
    def test1():
        #array = [50, 3, 10, 7, 40, 80]
        array = [15, 27, 14, 38, 63, 55, 46, 65, 85]
        ans = Prob.longestDecreasingSubsequence(array)
        print("test1: ans: ", ans)

Prob.test1()
