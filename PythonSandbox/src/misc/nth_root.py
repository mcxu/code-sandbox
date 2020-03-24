'''
Find the nth root of value x.
'''

class Prob:
    '''
    Using binary search.
    Time complexity: O(log_2(x)), since the binary search searches initially using [0,x]
    Space complexity: O(1), since the med variable just stores the median after each iteration.
    '''
    @staticmethod
    def nthRoot(n, x):
        lo = 0
        hi = x
        acc = .000001 # accuracy of calculation
        med = (lo + hi)/2
        i = 0
        while abs(med**n - x) > acc:
            print("med: ", med)
            if med**n > x:
                hi = med
            else:
                lo = med
            med = (lo + hi)/2
            i += 1
        return med
    
    @staticmethod
    def test1(alg):
        n = 3 # root
        x = 1001
        r = alg(n, x)
        print("r: ", r)

alg = Prob.nthRoot
Prob.test1(alg)