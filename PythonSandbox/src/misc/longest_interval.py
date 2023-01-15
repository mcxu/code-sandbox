'''
Find largest interval, including overlapping ones:
Given:
intervals =  [[-10, -8], [-5, 3], [2, 7], [3, 8], [9, 12], [15, 23], [17, 24], [27, 30]]
Return: 13 ([-5,3],[2,7],[3,6] -> -5 to 8 -> 13)
'''

def findLargestInterval(intervals):
    intervals = sorted(intervals, key=lambda x:x[0])
    s = 0 # save starting point of current continuous series of overlaps
    maxIntervalSoFar = 0
    currInterval = 0
    for i in range(len(intervals)-1):
        curr = intervals[i]
        nxt = intervals[i+1]
        print("curr:{}, nxt:{}, saved:{}".format(curr,nxt,intervals[s]))
        if curr[1] >= nxt[0]:
            if nxt[1] <= curr[1]:
                currInterval = curr[1]-intervals[s][0]
                print("ci A: ", currInterval)
            else:
                currInterval = nxt[1]-intervals[s][0]
                print("ci B: ", currInterval)
        else:
            s = i+1
            print("s incremented: ", s)
        
        if currInterval > maxIntervalSoFar:
            maxIntervalSoFar = currInterval

    print("saved after: ", s)
    # evaluate last interval
    if intervals[-1][1]-intervals[s][0] > maxIntervalSoFar:
        maxIntervalSoFar = intervals[-1][1]-intervals[s][0]

    return maxIntervalSoFar

def testsort():
    intervals = [[-10,-8],[-5,3],[2,7],[3,6],[9,12],[15,23],[17,24],[27,30]]
    intervals = sorted(intervals, key=lambda x:x[0])
    print("sorted: ", intervals)
#testsort()

def test_findLargestInterval():
    intervals =  [[-10, -8], [-5, 3], [2, 7], [3, 8], [9, 12], [15, 23], [17, 24], [27, 30]]
    #intervals = [[-10, -8], [-5, 3], [2, 7], [3, 8], [9, 12], [15, 23], [17, 28], [27, 300]] # 285
    res = findLargestInterval(intervals)
    print("res: ", res)
test_findLargestInterval()