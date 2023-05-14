'''
L1: [(1,2), (3,9)]
L2: [(4,6), (8,10), (11,12)]
output: [(1,2), (3,10), (11,12)]
'''
def mergeTuples(L1, L2):
    mergedTups = []

    # merge tuples as is by their first values
    p1, p2 = 0, 0
    while p1 < len(L1) and p2 < len(L2):
        tup1, tup2 = L1[p1], L2[p2]
        if tup1[0] <= tup2[0]:
            mergedTups.append(tup1)
            p1 += 1
        elif tup1[0] > tup2[0]:
            mergedTups.append(tup2)
            p2 += 1
    
    # account for trailing tuples
    if p1 < len(L1):
        mergedTups += L1[p1:]
    elif p2 < len(L2):
        mergedTups += L2[p2:]

    print("mergedTups: ", mergedTups)
    #[(1, 2), (3, 9), (4, 6), (8, 10), (11, 12)]

    # resolve overlapping tuples
    i = 0 
    while i < len(mergedTups)-1:
        currTup, nextTup = mergedTups[i], mergedTups[i+1]

        # current tuple completely overlapping next tuple
        if currTup[1] >= nextTup[0] and currTup[1] >= nextTup[1]: 
            mergedTups.pop(i+1)
            i -= 1
        # current tuple partially overlapping next tuple
        elif currTup[1] >= nextTup[0]:
            mergedTups[i] = (currTup[0], nextTup[1])
            i -= 1

        i += 1

    return mergedTups


def test_mergeTuples():
    L1 = [(1,2), (3,9)]
    L2 = [(4,6), (8,10), (11,12)]
    res = mergeTuples(L1, L2)
    print('res: ', res)

test_mergeTuples()
