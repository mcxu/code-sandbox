'''
Find the nth root of value x.
'''

class Prob:
    '''
    
    '''
    @staticmethod
    def nthRoot(n, x):
        lo = 0
        hi = x
        acc = .00000000001 # accuracy of calculation
        med = (lo + hi)/2
        while abs(med**2 - x) > acc:
            if med**n > x:
                hi = med
            elif med**n < x:
                lo = med
            med = (lo + hi)/2
        
        return med
    
    @staticmethod
    def test1(alg):
        n = 2 # root
        x = 3.14
        r = alg(n, x)
        print("r: ", r)

alg = Prob.nthRoot
Prob.test1(alg)