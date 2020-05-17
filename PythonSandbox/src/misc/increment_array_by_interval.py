'''
Given an input array. Given a list of [[interval], x]. 
The interval is a starting index and ending index, inclusive.
The value x is the amount to increment for its respective interval.
Return the output array after the appropriate interval increments.
Example:
input: 
arr = [0,1,1,2,2,1,1,0]
intervals = [
    [[1,4], 1],
    [[3,6], 2]
]
output: [0,2,2,5,5,3,3,0]
'''

class Solution:
    '''
    Let:
        n = len(intervals)
        r = interval with max range that exists in intervals.
        a = len(arr)
    Time: O(n*r + a)
    Space: O(r), since each unique index in the set of intervals is in incMap.
    '''
    def incrementArrayValues(self, arr, intervals):
        incMap = self.getIncMap(intervals) #O(n*r) time
        for i,_ in enumerate(arr):
            if i in incMap.keys():
                arr[i] += incMap[i]
        return arr

    def getIncMap(self, intervals):
        incMap = {} # index:delta to increment value at index in arr by.
        for i,interval in enumerate(intervals):
            intRange = interval[0]
            iStart = intRange[0]
            iEnd = intRange[1]
            x = interval[1]
            for j in range(iStart,iEnd+1):
                if j in incMap.keys():
                    incMap[j] += x
                else:
                    incMap[j] = x
        return incMap
    
    def test1(self):
        arr = [0,1,1,2,2,1,1,0]
        intervals = [
            [[1,4], 1],
            [[3,6], 2]]
        res = self.incrementArrayValues(arr, intervals)
        print("test1 res: ", res)

prob = Solution()
prob.test1()