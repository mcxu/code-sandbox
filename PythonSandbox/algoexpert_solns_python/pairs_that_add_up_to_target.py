"""
Given an array of numbers, find all pairs of numbers that add up to a target number.
https://www.geeksforgeeks.org/count-pairs-with-given-sum/#
"""

def findPairs(arr, target):
    numMap = {}
    for i,n in enumerate(arr):
        if n in numMap.keys():
            numMap[n].add(i)
        else:
            numMap[n] = set([i])

    print("numMap: ", numMap)

    pairs = []

    for i,n in enumerate(arr):
        print(f"--- outer for, i:{i}, n:{n}")
        otherNum = target-n
        if otherNum in numMap.keys():
            print(f"num {otherNum} found in keys")
            otherIndicesToRemove = set()
            currentIndicesToRemove = set()

            for otherIdx in numMap[otherNum]:
                if i != otherIdx:
                    pairs.append((n, otherNum))
                    otherIndicesToRemove.add(otherIdx)
                    currentIndicesToRemove.add(i)
            
            print("otherIndicesToRemove: ", otherIndicesToRemove)
            print("currentIndicesToRemove: ", currentIndicesToRemove)

            if otherNum in numMap.keys():
                numMap[otherNum] -= otherIndicesToRemove
                if not numMap[otherNum]:
                    numMap.pop(otherNum)

            if n in numMap.keys():
                numMap[n] -= currentIndicesToRemove
                if not numMap[n]:
                    numMap.pop(n)

            print("numMap after removal: ", numMap)
        print("numMap after iteration: ", numMap)
        print("pairs so far: ", pairs)

    return pairs

def test1():
    #arr = [1, 5, 7, -1]; target = 6 # expected (1,5) (7,-1)
    #arr = [1, 5, 7, -1, 5]; target = 6 # expected (1, 5), (7, -1) & (1, 5)
    #arr = [1, 1, 1, 1]; target = 2 # expected (1, 1), (1, 1), (1, 1)
    arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]; target = 11
    result = findPairs(arr, target)
    print("result: ", result)

test1()