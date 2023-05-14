'''
0,1 - Knapsack Problem

Given list of items with format [value, weight], and a weight capacity.
Choose items that maximize value while keeping weight <= capacity.
Output should be format: [max value, [indices of the chosen items]]

Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
Sample output: [10, [1, 3]]
'''
class KP:
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
    def knapsack01BruteForce(items, capacity):
        # handle 0 capacity:
        if not items or capacity<=0:
            return [0,[]]
        
        # create powerset of indices; which means set of subsets, 
        # and each subset contains indices in items. O(n*2^n) time.
        powerset = set([()]) # store sets of indices of subsets
        for i in range(len(items)):
            tempset = set()
            for st in powerset:
                subset = st + tuple([i])
                tempset.add(subset)
            powerset |= tempset 
        # print("powerset: ", powerset)
        
        totalReward = 0 # totals reward within a set of items
        maxItemIdxSubset = None
        for idxSubset in powerset: # O(2^n) time, since there are 2^n subsets in the powerset.
            [totRewardForSubset, totWtForSubset] = KP.getTotValAndWtFromIdxSubset(items, idxSubset) # O(n) time
            if totRewardForSubset>totalReward and totWtForSubset<=capacity:
                totalReward = totRewardForSubset
                maxItemIdxSubset = idxSubset
        return [totalReward, maxItemIdxSubset]
    
    @staticmethod
    def getTotValAndWtFromIdxSubset(items, idxSubset): # O(n) time.
        rewardSum = 0 # sum of values (rewards) in this set of items
        weightSum = 0 # sum of weights in this set of items
        for idx in idxSubset: 
            itm = items[idx]
            rewardSum += itm[0]
            weightSum += itm[1]
        return [rewardSum, weightSum]
    
#---------------------------------------------------------------------------------
    '''
    Brute force, recursive. Only returns the 
    maximum value of the items.
    '''
    @staticmethod
    def knapsack01_BFRecMaxValOnly(items, capacity):

        # items, remaining capacity, index that starts with 0
        def helper(items, remCap, i):
            if i >= len(items) or remCap <= 0:
                return 0
            
            currItem = items[i]
            value, weight = currItem[0], currItem[1]

            if weight > remCap:
                # we need to reject the item
                rejectItem = helper(items, remCap, i+1)
                return rejectItem

            # otherwise, we try both of accept and reject and choose the one that returns the max reward
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
    def knapsack01_BFRecWithItemIndices(items, capacity):
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
    Iterative, Dynamic Programming
    Stores solutions to subproblems for some capacity and range of items.
    for example a row means all items including 0 items up to that item in the row.
    
    items(y)                    capacities (x)
             [0    1    2    3    4    5    6    7    8    9    10]
    [empty]   0    0    0    0    0    0    0    0    0    0    0
      [1,2]   0
      [4,3]   0
      [5,6]   0
      [6,7]   0
    '''
    @staticmethod
    def knapsack01_IterativeDP(items, capacity):
        memo = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
        
        for y in range(1, len(memo)):
            for x in range(1, len(memo[y])):
                print("y={}, x={}".format(y,x))
                currItem = items[y-1]
                print("    currItem: ", currItem)
                currItemValue, currItemWeight = currItem[0], currItem[1] 
                
                valueIfLeaveItem = memo[y-1][x]
                print("    valueIfLeaveItem: ", valueIfLeaveItem)
                
                valueIfTakeItem = 0
                if x-currItemWeight >= 0:
                    valueIfTakeItem = memo[y-1][x-currItemWeight] + currItemValue
                print("    valueIfTakeItem: ", valueIfTakeItem)
                
                memo[y][x] = max(valueIfLeaveItem, valueIfTakeItem)
        
        chosenIndices = []
        KP.backtrackDPMemo(memo, len(items), capacity, items, chosenIndices)
        #print("chosenIndices filled: ", chosenIndices)
        
        return [memo[len(items)][capacity], chosenIndices]
        
        
    @staticmethod
    def backtrackDPMemo(memo, y, x, items, chosenIndices):
        if y==0 or x==0:
            return
        
        currRewardVal = memo[y][x]
        print("backtrackDPMemo: currRewardVal: ", currRewardVal)
        aboveRewardVal = memo[y-1][x]
        
        prevItem = items[y-1]
        prevItemWeight = prevItem[1]
        
        if currRewardVal > aboveRewardVal:
            # The current reward being greater than the previous reward
            # implies that the current item was taken.
            chosenIndices.insert(0, y-1)
            x = x - prevItemWeight

        KP.backtrackDPMemo(memo, y-1, x, items, chosenIndices)
    
    #---------------------------------------------------------------------------------
        
def test1(alg):
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    #Sample output: [10, [1, 3]]
    res = alg(items, capacity)
    print("test1 res: ", res)

def test2(alg):
    items = [[1, 2], [4, 3], [5, 6], [6, 7], [8,5], [3,3], [7,2]]
    #          0        1      2        3      4      5      6
    capacity = 10
    # output: test2 res:  [19, [1, 4, 6]]
    res = alg(items, capacity)
    print("test2 res: ", res) 

def test3(alg):
    items = [[1, 2], [4, 3], [1, 2]]
    #          0        1      2    
    capacity = 10
    # output: test2 res:   [6, [0, 1, 2]]
    res = alg(items, capacity)
    print("test3 res: ", res) 

#alg = KP.knapsack01BruteForce
#alg = KP.knapsack01_BFRecMaxValOnly
#alg = KP.knapsack01_BFRecWithItemIndices
alg = KP.knapsack01_IterativeDP

#test1(alg)
#test2(alg)
test3(alg)
