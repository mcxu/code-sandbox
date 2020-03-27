'''
0,1 - Knapsack Problem

Given list of items with format [value, weight], and a weight capacity.
Choose items that maximize value while keeping weight <= capacity.

Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
Sample output: [10, [1, 3]]
'''
class Prob:
    '''
    Brute force method, using powerset of indices from items array.
    For example, subset in powerset of [0,3] translates to [[1,2],[6,7]] in items array.
    
    Let n = len(items)
    Time complexity:
        Powerset takes O(n*2^n) time: outer for iterates through n items, 
        inner for iterates 2^n more items in indicesSet each time it is entered. -> O(n*2^n) time.
        In the 2nd outer for loop to compute max value, it iterates through 2^n subsets.
        In the indexSetToTotalValAndWeight() function, it takes O(n) time to compute value and weight sums. -> O(n*2^n) time.
        Total: O(n*2^n) + O(n*2^n), which is still O(n*2^n) time.
    Space complexity:
        O(2^n), since there are that many subsets produced from n items. And all these results are stored in an array (indicesSet).
    '''
    @staticmethod
    def knapsackProblem(items, capacity):
        # handle 0 capacity:
        if not items or capacity<=0:
            return [0,[]]
        
        # create powerset; which means set of subsets, and each subset contains indices in items. O(n*2^n) time.
        indicesSet = [[]] # store sets of indices of subsets
        for i in range(len(items)):
            for j in range(len(indicesSet)):
                subset = indicesSet[j] + [i]
                indicesSet.append(subset)
        print("indicesSet: ", indicesSet)
        print("indicesSet length: ", len(indicesSet))
        
        maxVal = 0 # totals within a set of items
        maxItemIndices = None
        for i in range(len(indicesSet)): # O(2^n) time, since there are 2^n subsets in the powerset.
            indexSet = indicesSet[i] # like [0,1,2,3], each value corresponds to the index of an item in items array
            #print("indexSet: ", indexSet)
            [itmSetVal, itmSetWeight] = Prob.indexSetToTotalValAndWeight(items, indexSet) # O(n) time
            #print("A: ", [itmSetVal, itmSetWeight])
            if itmSetVal>maxVal and itmSetWeight<=capacity:
                maxVal = itmSetVal
                # print("maxVal: ", maxVal)
                # print("maxWeight: ", maxWeight)
                maxItemIndices = indexSet
        return [maxVal, maxItemIndices]
    
    @staticmethod
    def indexSetToTotalValAndWeight(items, indexSet): # O(n) time.
        itmSetVal = 0 # sum of values in this set of items
        itmSetWeight = 0 # sum of weights in this set of items
        for j in range(len(indexSet)):
            itmInd = indexSet[j]  
            itm = items[itmInd]
            itmSetVal += itm[0]
            itmSetWeight += itm[1]
        return [itmSetVal, itmSetWeight]
    
    #---------------------------------------------------------------------------------
    
    @staticmethod
    def test1():
        items = [[1, 2], [4, 3], [5, 6], [6, 7]]
        capacity = 10
        #Sample output: [10, [1, 3]]
        res = Prob.knapsackProblem(items, capacity)
        print("test1 res: ", res)

Prob.test1()
        