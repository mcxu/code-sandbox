'''
x^n
'''
# time complexity: O(log n): each time n is //2
# space complexity: O(log n); correlates with the time complexity with regards to 
# the number of recursive calls that are put on the call stack.
def powRecursive(x: float, n: int) -> float:
    res = powHelper(x, abs(int(n)))
    if n < 0:
        return 1/res
    return res

def powHelper(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    if n % 2 == 0: # even number of factors
        return powHelper(x, n//2) * powHelper(x, n//2)
    else:
        return powHelper(x, n//2) * powHelper(x, n//2) * powHelper(x, 1)

#==============================================================

# time complexity: O(log n)
# space complexity: O(1)
def powExponentiation(x, n):
    ans = 1.0
    nn = n
    if nn < 0:
        nn = -1 * nn
        
    while nn:
        if nn % 2 == 1: # if nn is odd
            ans = ans * x
            nn = nn - 1
        else: # if nn is even
            x = x * x
            nn = nn // 2
    
    if n < 0:
        ans = 1.0 / ans
    return ans

def test_pow():
    #x = 2; n = -5
    #x = 2; n = 0
    x = 4; n = 8
    result = powRecursive(x, n)
    #result = powExponentiation(x,n)
    print("result: ", result)

test_pow()
