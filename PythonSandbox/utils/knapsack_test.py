"""
items:
[reward, weight]
Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
Sample output: [10, [1, 3]]
"""
def knapSack(items, capacity):
    # stores reward for (item n, capacity c)
    memo = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]

    for y in range(1, len(items)+1):
        for x in range(1, capacity+1):
            currItem = items[y-1]
            currItemReward, currItemWeight = currItem[0], currItem[1]

            valueIfLeaveItem = memo[y-1][x]

            valueIfTakeItem = 0
            if x-currItemWeight >= 0:
                valueIfTakeItem = memo[y-1][x-currItemWeight] + currItemReward
            
            memo[y][x] = max(valueIfLeaveItem, valueIfTakeItem)
    
    printMatrix(memo)

    # to get the max reward for the largest subproblem (the problem itself)
    maxReward = memo[-1][-1]
    chosenItems = []
    backtrackMemo(memo, items, len(items), capacity, chosenItems)
    return [maxReward, chosenItems]

def backtrackMemo(memo, items, y, x, chosenItems):
    if y == 0 or x == 0:
        return
    
    currReward = memo[y][x]
    prevReward = memo[y-1][x]

    prevItem = items[y-1]
    prevItemWeight = prevItem[1]

    if currReward > prevReward:
        chosenItems.append(y-1)
        x = x - prevItemWeight
    
    backtrackMemo(memo, items, y-1, x, chosenItems)

def printMatrix(mat):
    print("---- matrix ----")
    for row in mat:
        print(row)
    print("----------------")

def test():
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10

    result = knapSack(items, capacity)
    print("result: ", result)

test()