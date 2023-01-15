'''
Remove repeated chars from a string.
s = "aadddefwgg"
output = "adefwg"

O(n) time complexity
O(n) space complexity
'''
def removeRepeatedChars(s):
    sList = list(s)

    i = 0
    while i < len(sList)-1:
        print("i=", i)
        removeRepeatsFromInd(sList, i)
        i += 1
    return "".join(sList)
    
def removeRepeatsFromInd(sList, i):
    curr = sList[i]
    nxt = sList[i+1]
    while curr==nxt:
        sList.pop(i)
        print("sList popped: ", sList)
        curr = sList[i]
        if i+1 > len(sList)-1: return
        nxt = sList[i+1]

def test1():
    s = "aadddefwgg"
    res = removeRepeatedChars(s)
    print("res: ", res)
test1()