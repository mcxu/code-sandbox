'''
Dutch flag problem
Sort an array of 0s, 1s and 2s
'''

def dutchFlag(arr):
    lo = 0
    hi = len(arr)-1
    mid = 0
    while mid <= hi:
        if arr[mid]==0:
            arr[lo],arr[mid]=arr[mid],arr[lo]
            lo += 1
            mid += 1
        elif arr[mid]==1:
            mid += 1 
        else:
            arr[hi],arr[mid]=arr[mid],arr[hi]
            hi -= 1
    return arr

def test1():
    arr = [0, 1, 2, 0, 1, 2]
    res = dutchFlag(arr)
    print("res: ", res)

test1()
