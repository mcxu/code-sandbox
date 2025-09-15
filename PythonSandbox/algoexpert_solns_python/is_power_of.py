'''
Function that determines whether a number n is power of b.
log_b(n) = x --> x = log_e(n)/log_e(b)
if x is an integer, then true, else false.
'''
import math

def isnPowerOfb(n,b):
    x = math.log(n)/math.log(b)
    if x == int(x):
        return True
    return False

res = isnPowerOfb(100,10)
print("res: ", res)

res = isnPowerOfb(81,3)
print("res: ", res)