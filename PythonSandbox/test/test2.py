'''
P1 D1 P2 D2 ...
P3 P1 D1 D3 P2 D2
D1 P1
'''
#pd = [P3 P1 D1 D3 P2 D2]
#pd = [D1 P1]
'''
pdMap:
    1:"D"
n = len(pd)
Time: O(n + n/2) which is O(n)
Space: O(n/2) which is O(n)
'''
 
def isValidOrders(pd):
    if not pd:
        return True
    pdMap = {}
    for i,item in enumerate(pd):
        ch = item[0]
        num = item[1]
        print("ch: {}, num: {}".format(ch, num))
        print("pdMap: ", pdMap)
        if num not in pdMap.keys():
            if ch == "D":
                return False
            pdMap[num] = ch
        else:
            if ch == "P":
                return False
            else:
                if pdMap[num] == "P":
                    pdMap[num] = "D"
        
    for key in pdMap.keys():
        if pdMap[key] == "P":
            return False
    return True

def test1():
    pd = ["P1","D1", "P1"]
    res = isValidOrders(pd)
    print("res: ", res)
test1()
def test2():
    #pd = ["P1","D1"]
    #pd = ["D1", "P1"]
    #pd = ["P1"]
    res = isValidOrders(pd)
    print("res: ", res)
#test2()