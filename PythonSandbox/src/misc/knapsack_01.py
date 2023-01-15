'''
0,1 - Knapsack Problem

Given list of items with format [value, weight], and a weight capacity.
Choose items that maximize value while keeping weight <= capacity.
Output should be format: [max value, [indices of the chosen items]]

Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
Sample output: [10, [1, 3]]
'''
class Prob:
    '''
    Brute force method, using powerset of indices from items array.
    For example, subset in powerset of [0,3] translates to [[1,2],[6,7]] in items array.
    
    Let n = len(items)
    Time complexity:
        Powerset takes O(n*2^n) exponential time: outer for iterates through n items, 
        inner for iterates 2^n more items in indicesSet each time it is entered. -> O(n*2^n) time.
        In the 2nd outer for loop to compute max value, it iterates through 2^n subsets.
        In the indexSetToTotalValAndWeight() function, it takes O(n) time to compute value and weight sums. -> O(n*2^n) time.
        Total: O(n*2^n) + O(n*2^n), which is still O(n*2^n) time.
    Space complexity:
        O(2^n), since there are that many subsets produced from n items. And all these results are stored in an array (indicesSet).
    '''
    @staticmethod
    def knapsack01BF(items, capacity):
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
    '''
    Brute force, recursive. Only returns the 
    maximum value of the items.
    '''
    @staticmethod
    def knapsack01BFRecMaxVal(items, capacity):
        def helper(items, remCap, i):
            if i >= len(items) or remCap <= 0:
                return 0
            
            currItem = items[i]
            value = currItem[0]
            weight = currItem[1]

            if weight > remCap:
                return helper(items, remCap, i+1)

            acceptItem = helper(items, remCap-weight, i+1) + value
            rejectItem = helper(items, remCap, i+1)
            return max(acceptItem, rejectItem)
        
        return helper(items, capacity, 0)

    #---------------------------------------------------------------------------------
    '''
    Brute force, recursive. Also returns item indices.
    Time complexity: O(2^n), since each call of the helper results in 2x calls of the helper, one for include item, one for exclude item.
    Space complexity: O(n), since there are a max of n calls of the helper on the call stack.
    '''
    @staticmethod
    def knapsack01BFRec2(items, capacity):
        
        # remCap means remaining capacity. This starts out equal to capacity at the root helper call.
        # vii: valid item indices; keep track of which indices were included.
        def helper(items, remCap, i, totVal, vii):
            
            if i >= len(items) or remCap <= 0:
                # there is no additional value that can be added, return 0 for value
                return [totVal, vii]
            
            item = items[i]
            itemValue = item[0]
            itemWeight = item[1]
            
            # if item weight is greater than remaining capacity, you can't add the value of the time to the knapsack
            # so return the knapsack problem using the same remaining capacity and move to the next item.
            if itemWeight > remCap:
                return helper(items, remCap, i+1, totVal, vii)
            
            # Recursive call for additional value by including the current item.
            # Including the current item means subtracting the weight of the current item from the remaining capacity.
            # Also need to append the current index to vii to keep track of which item was included.
            addValueWithCurrItem = helper(items, remCap-itemWeight, i+1, totVal+itemValue, vii+[i])
            
            # Recursive call for additional value by excluding the current item.
            # Excluding the current time means not changing remaining capacity, and not appending current item index to vii.
            addValueWithoutCurrItem = helper(items, remCap, i+1, totVal, vii)
            
            if addValueWithCurrItem[0] > addValueWithoutCurrItem[0]:
                return addValueWithCurrItem
            else:
                return addValueWithoutCurrItem
            
        # remaining capacity at beginning is the total capacity itself.
        totVal = 0
        vii = []
        maxValueAndIndices = helper(items, capacity, 0, totVal, vii)
        return maxValueAndIndices
        
    #---------------------------------------------------------------------------------
    
    '''
    Recursive, with Memoization
    TODO: returning the memo gives wrong answer, but leaving it out gives correct answer.
        'answer' as in [totalvalue, [indices]]
    '''
    @staticmethod
    def knapsack01RecMemo(items, capacity):
        
        def helperMemo(items, remCap, i, totVal, vii, memo):
            nonlocal c
            c+= 1
            
            if i >= len(items) or remCap <= 0:
                return [totVal, vii]
            
            print("-----------\ni=", i)
            print("remCap: ", remCap)
            
#             print("item memo print:")
#             for row in memo:
#                 print("    ", row)
            
            if memo[i][remCap]:
                print("previously memoized solution found: ", memo[i][remCap])
                return memo[i][remCap]
            
            result = [0,[]]
            
            item = items[i]
            itemValue = item[0]
            itemWeight = item[1]
            print("item: ", item)
            
            if itemWeight > remCap:
                print("AAA")
                result = helperMemo(items, remCap, i+1, totVal, vii, memo)
            else:
                print("BBB")
                addValueWithCurrItem = helperMemo(items, remCap-itemWeight, i+1, totVal+itemValue, vii+[i], memo)
                addValueWithoutCurrItem = helperMemo(items, remCap, i+1, totVal, vii, memo)
                
                if addValueWithCurrItem[0] > addValueWithoutCurrItem[0]:
                    print("A: i={}, remCap={}".format(i, remCap))
                    result = addValueWithCurrItem
                else:
                    print("B: i={}, remCap={}".format(i, remCap))
                    result = addValueWithoutCurrItem
            
            if not memo[i][remCap]:
                memo[i][remCap] = result
            elif memo[i][remCap] and result[0] > memo[i][remCap][0]:
                memo[i][remCap] = result
            print("B memo items: i={}, remCap={}, memo: {}".format(i, remCap, memo[i][remCap]))
            
            print("item memo print:")
            for row in memo:
                print("    ", row)
                
            return result
        
        memo = [[ None for _ in range(capacity+1) ] for _ in range(len(items))]
        #indMemo = memo.copy()
        startIndex = 0
        c = 0
        totVal = 0
        vii = []
        result = helperMemo(items, capacity, startIndex, totVal, vii, memo)
        print("c ==== ", c)
        return result
    
    #---------------------------------------------------------------------------------

    '''
    Iterative, Dynamic Programming
    '''
    @staticmethod
    def knapsack01IterativeDP(items, capacity):
        '''
        stores solutions to subproblems for some capacity and range of items.
        for example a row means all items including 0 items up to that item in the row.
        
        items(y)                    capacities (x)
               [0    1    2    3    4    5    6    7    8    9    10]
           []   0    0    0    0    0    0    0    0    0    0    0
        [1,2]   0
        [4,3]   0
        [5,6]   0
        [6,7]   0
        '''
        memo = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
        
        for y in range(1, len(memo)):
            for x in range(1, len(memo[y])):
                print("y={}, x={}".format(y,x))
                currItem = items[y-1]
                print("    currItem: ", currItem)
                currItemValue = currItem[0]
                currItemWeight = currItem[1]
                
                valueIfLeaveItem = memo[y-1][x]
                print("    valueIfLeaveItem: ", valueIfLeaveItem)
                
                valueIfTakeItem = 0
                if x-currItemWeight >= 0:
                    valueIfTakeItem = memo[y-1][x-currItemWeight] + currItemValue
                print("    valueIfTakeItem: ", valueIfTakeItem)
                
                memo[y][x] = max(valueIfLeaveItem, valueIfTakeItem)
        
        print("memo after: ")
        for row in memo:
            print(row)
        
        chosenIndices = []
        Prob.backtrackDPMemo(memo, len(items), capacity, items, chosenIndices)
        print("chosenIndices filled: ", chosenIndices)
        
        return [memo[len(items)][capacity], chosenIndices]
        
        
    @staticmethod
    def backtrackDPMemo(memo, y, x, items, chosenIndices):
        if y==0 or x==0:
            return
        
        currMemoVal = memo[y][x]
        aboveMemoVal = memo[y-1][x]
        
        item = items[y-1]
        itemWeight = item[1]
        
        if currMemoVal > aboveMemoVal:
            # this means that the current item was taken.
            chosenIndices.insert(0, y-1)
            x = x - itemWeight
            y = y-1
        else:
            y = y-1
        
        Prob.backtrackDPMemo(memo, y, x, items, chosenIndices)
    
    #---------------------------------------------------------------------------------
        

    @staticmethod
    def test1(alg):
        items = [[1, 2], [4, 3], [5, 6], [6, 7]]
        capacity = 10
        #Sample output: [10, [1, 3]]
        res = alg(items, capacity)
        print("test1 res: ", res)
    
    @staticmethod
    def test2(alg):
        items = [[1, 2], [4, 3], [5, 6], [6, 7], [8,5], [3,3], [7,2]]
        #          0        1      2        3      4      5      6
        capacity = 10
        # output: test2 res:  [19, [1, 4, 6]]
        res = alg(items, capacity)
        print("test2 res: ", res) 

    @staticmethod
    def test3(alg):
        items = [[1, 2], [4, 3], [1, 2]]
        #          0        1      2    
        capacity = 10
        # output: test2 res:   [6, [0, 1, 2]]
        res = alg(items, capacity)
        print("test3 res: ", res) 

#alg = Prob.knapsack01BF
#alg = Prob.knapsack01BFRec
alg = Prob.knapsack01BFRecMaxVal
#alg = Prob.knapsack01RecMemo
#alg = Prob.knapsack01IterativeDP

Prob.test1(alg)
#Prob.test2(alg)
#Prob.test3(alg)
