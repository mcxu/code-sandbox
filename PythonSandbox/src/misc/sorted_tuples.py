'''
L1: [(1,2), (3,9)]
L2: [(4,6), (8,10), (11,12)]
output: [(1,2), (3,10), (11,12)]
'''
def overLappingTuples(L1, L2):
    p1 = 0
    p2 = 0
    outputList = []
    while p1 < len(L1) and p2 < len(L2):
        tup1 = L1[p1]; tup2 = L2[p2]
        overlapStatus = isOverlap(tup1, tup2)
        if overlapStatus == 0:
            if tup1[1] < tup2[0]:
                outputList.append(tup1)
                p1 += 1
            elif tup2[1] < tup1[0]:
                outputList.append(tup2)
                p2 += 1
        elif overlapStatus == 1:
            outputList.append((tup1[0], tup2[1]))
            p1 += 1; p2 += 1
        elif overlapStatus == 2:
            outputList.append((tup2[0], tup1[1]))
            p1 += 1; p2 += 1
        elif overlapStatus == 3:
            p2 += 1
        elif overlapStatus == 4:
            p1 += 1
    if p1 < len(L1):
        outputList += L1[p1:]
    elif p2 < len(L2):
        outputList += L2[p2:]
    return outputList

'''
returns 0 if not overlap
returns 1 if t1 and t2 partially overlaps, and t2 is the higher tuple
returns 2 if t1 and t2 partially overlaps, and t1 is the higher tuple
returns 3 if t1 completely overlaps t2
returns 4 if t2 completely overlaps t1
'''
def isOverlap(t1, t2):
    if t2[0] > t1[1] or t2[1] < t1[0]:
        return 0
    elif t1[0] <= t2[0] and t1[1] >= t2[1]:
        return 3
    elif t1[0] >= t2[0] and t1[1] <= t2[1]:
        return 4
    elif t2[0] <= t1[1] and t2[1] > t1[1]:
        return 1
    elif t1[0] <= t2[1] and t1[1] > t2[0]:
        return 2


def testisOverlap():
    #t1 = (1,2); t2 = (4,6)
    #t2 = (1,2); t1 = (4,6)
    #t1 = (1,4); t2 = (3,5)
    #t2 = (1,4); t1 = (3,5)
    #t1 = (1,10); t2 = (3,7)
    t2 = (1,10); t1 = (3,7)
    res = isOverlap(t1, t2)
    print("res1: ", res)

#testisOverlap()

def test1():
    L1 = [(1,2), (3,9)]
    L2 = [(4,6), (8,10), (11,12)]
    res = overLappingTuples(L1, L2)
    print("res: ", res)

test1()