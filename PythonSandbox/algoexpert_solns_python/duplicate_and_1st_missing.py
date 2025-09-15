'''
Find duplicate and first missing number in array.
[1,1,2,3,4]
'''

def find(arr):
    arr = sorted(arr)
    dInd = 0
    
    for i in range(len(arr)-1):
        curr = arr[i]
        nxt = arr[i+1]
        if curr == nxt:
            dInd = i
            break
    
    missingNum = -1
    for i in range(1, len(arr)):
        curr = arr[i]
        prev = arr[i-1]
        if curr > prev and curr > prev+1:
            missingNum = prev+1
            break
    
    if missingNum == -1:
        missingNum = arr[-1]+1

    return [arr[dInd], missingNum]

def test1():
    #arr = [1,1,2,3,4]
    arr = [1,2,2,3,4,5,7]
    res = find(arr)
    print('res: ', res)
test1()
