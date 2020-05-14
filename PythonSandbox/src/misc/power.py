'''
x^n
'''

def pow(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    p = x
    for i in range(1, abs(n)):
        p *= x
    
    if n < 0:
        return float(1/p)

    return p

def powRecursive(x,n):
    if n < 0:
        return x**n

    n = int(n)
    if n == 0:
        return 1
    if n == 1:
        return x
    
    isOdd = int(n % 2) # number of 'x's
    if isOdd == 0:
        # even number of 'x's
        return powRecursive(x,n/2)*powRecursive(x,n/2)
    else:
        return powRecursive(x,n/2)*powRecursive(x,n/2)*powRecursive(x,1)

def test_pow():
    x = 2
    n = -5
    result = pow(x,n)
    #result = powRecursive(x,n)
    print("result: ", result)

test_pow()
