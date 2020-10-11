def numPaths(y, x):
    if y==0 and x==0:
        return 1
    if y<0 or x<0:
        return 0
    
    right = numPaths(y, x-1)
    down = numPaths(y-1, x)
    return right+down

def test1():
    y = 2
    x = 3
    res = numPaths(y, x)
    print("res: ", res)
test1()