# Complete the 'minSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num
#  2. INTEGER k
#

import heapq
def minSum(num, k):
    heapArr = [-x for x in num]
    print('heapArr: ', heapArr)
    # max heap using the negatives
    heapq.heapify(heapArr)
    print('heapArr after heapify: ', heapArr)
    
    for i in range(k): 
        minVal = heapArr[0]
        print("minVal: ", minVal)
        minValUpdated = int((minVal-1)/2)
        heapq.heapreplace(heapArr, minValUpdated)
        print("heap after: ", heapArr)

    print("headArr final: ", heapArr)
    heapArr = sum([-x for x in heapArr])
    return heapArr

num = [10,20,7]
k= 4
print(minSum(num,k))