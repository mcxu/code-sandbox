'''
do 2 intervals overlap? returns true if yes, false otherwise.
'''

def intervalsOverlap(A, B):
    if A[0] <= B[0] <= A[1] or A[0] <= B[1] <= A[1]:
        return True
    return False

def test():
    # A = [1,3] # B = [2,4]
    # A,B = [5,10], [3,6]
    A,B = [1,5], [6,10]
    result = intervalsOverlap(A,B)
    print("result: ", result)

test()