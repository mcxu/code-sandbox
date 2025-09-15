'''
Largest Range of Consecutive Numbers in Array

Given array, return a range in the format [low num, high num],
which represents the largest range of consecutive numbers in the array.

Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample output: [0, 7]
'''

class Prob:
    '''
    Time complexity: O(n) since all of these loops and the max() iterate through entire array.
    Space complexity: O(n) since the rangeMap stores at most n keys and n values.
    '''
    @staticmethod
    def largestRange(array):
        rangeMap = {}
        
        for v in array:
            nextVal = v + 1
            if nextVal in array:
                rangeMap[v] = nextVal
        print("rangeMap: ", rangeMap)
        
        if not rangeMap:
            print("rangeMap empty")
            return [array[0], array[0]]
        
        for v in array:
            if v in rangeMap.keys():
                nextVal = v+1
                while nextVal in rangeMap.keys():
                    rangeMap[v] = rangeMap[nextVal]
                    print("rangeMap B: ", rangeMap)
                    nextVal += 1
        print("rangeMap C: ", rangeMap)
        
        maxRangeKey = max(rangeMap.keys(), key= lambda x: rangeMap[x] - x)
        print("maxRangeKey: ", maxRangeKey)
        return [maxRangeKey, rangeMap[maxRangeKey]]
    
    @staticmethod
    def test1():
        #array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
        #array = [1]
        #array = [1,3,5]
        #array = [1,3,5,6,7,9,10,11,12]
        array = [3,4,5,6,7]
        r = Prob.largestRange(array)
        print("test1: r: ", r)

Prob.test1()