"""
Input: 
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Output: 
1 2 4 3 5 7 6 8 9
"""
def getMatrixDiagonals(m):
    outputSequence = []
    
    # starting point: every number in top row
    for i in range(len(m[0])):
        outputSequence += getDiagonal(m, 0, i)
    
    # starting point: last column, except the top num
    for i in range(1, len(m)):
        outputSequence += getDiagonal(m, i, len(m[0])-1)
    
    # print("outputSequence: ", outputSequence)
    return outputSequence

"""
Get diagonal from starting point. Go down-left.
"""
def getDiagonal(m, y, x):
    diagNums = []
    while y < len(m) and x >= 0:
        diagNums.append(m[y][x])
        y += 1
        x -= 1
    return diagNums


def test():
    A = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    
    res = getMatrixDiagonals(A)
    print("res: ", res)

    resStr = ",".join([str(x) for x in res])
    print("printedOutputSequence: ", resStr)

test()