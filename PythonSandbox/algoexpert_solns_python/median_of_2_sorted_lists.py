def med_2_sorted_lists(l1, l2):
    i,j = 0,0

    mergedList = []

    while i < len(l1) and j < len(l2):
        v1, v2 = l1[i], l2[j]
        if v1 <= v2:
            mergedList.append(v1)
            i += 1
        elif v1 >= v2:
            mergedList.append(v2)
            j += 1
    
    if i == len(l1):
        mergedList += l2[j:]
    elif j == len(l2):
        mergedList += l1[i:]
    
    print("mergedList: ", mergedList)

    # find median
    # if even number of elements
    if len(mergedList) % 2 == 0:
        tot = mergedList[len(mergedList)//2 - 1] + mergedList[len(mergedList)//2]
        return tot/2

    # if odd number of elements
    return mergedList[len(mergedList)//2]

def test():
    l1 = [1,3,5]
    l2 = [2,4,6,8,10]
    res = med_2_sorted_lists(l1, l2)
    print("res: ", res)

test()
